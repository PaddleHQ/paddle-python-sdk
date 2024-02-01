from hashlib import sha256
from hmac    import HMAC, compare_digest, new as hmac_new

from paddle_billing.Logger import get_logger

from paddle_billing.Notifications.Secret import Secret


class PaddleSignature:
    def __init__(self):
        """
        Verifies the integrity of a Paddle signature
        """
        self.log = get_logger()


    @property
    def HASH_ALGORITHM_1(self):  # noqa N802
        return 'h1'

    @property
    def HEADER(self):  # noqa N802
        return 'Paddle-Signature'

    @property
    def TIMESTAMP(self):  # noqa N802
        return 'ts'


    @staticmethod
    def parse(signature_header: str) -> tuple:
        """
        Parse the Paddle-Signature header to extract the timestamp and signature

        @param   signature_header:  The Paddle-Signature key=value from the webhook event's headers
        @return:                    A tuple containing (timestamp, signature)
        """
        components = {
            PaddleSignature().TIMESTAMP: 0,
            'hashes':                    {PaddleSignature().HASH_ALGORITHM_1: []},
        }

        for key_value_pair in signature_header.split(";"):
            if '=' in key_value_pair:
                key, value = key_value_pair.split('=')

                if key == PaddleSignature().TIMESTAMP:
                    components[PaddleSignature().TIMESTAMP] = value
                elif key == PaddleSignature().HASH_ALGORITHM_1:
                    components['hashes'][PaddleSignature().HASH_ALGORITHM_1].append(value)
                else:
                    raise ValueError(f"Unrecognized Paddle-Signature key")

        return int(components[PaddleSignature().TIMESTAMP]), components['hashes']


    @staticmethod
    def calculate_hmac(secret_key: str, data: bytes) -> HMAC:
        return hmac_new(secret_key.encode('utf-8'), data, sha256)


    def __do_comparison(self, generated_signature: str, signature: str) -> bool:
        self.log.debug(f"Comparing received Paddle signature '{signature}' to our calculated signature: '{generated_signature}'")

        return compare_digest(generated_signature, signature)


    def __do_verify(self, timestamp: str, signatures: list[str], raw_body: str, secret_key: Secret) -> bool:
        """
        Verifies an individual secret key against a Paddle-Signature header.
        Called by PaddleSignature.verify()

        @param signatures: The Paddle-Signature header
        @param raw_body:   Raw body of the webhook request
        @param secret_key: A Paddle secret key: https://developer.paddle.com/webhooks/signature-verification#get-secret-key
        @return:           True on verification success, False on verification failure
        """
        new_body_to_verify  = f"{timestamp}:{raw_body}".encode('utf-8')
        generated_signature = PaddleSignature.calculate_hmac(secret_key.secret_key, new_body_to_verify).hexdigest()
        integrity           = False

        for signature in signatures:
            integrity_result = self.__do_comparison(generated_signature, signature)
            if integrity_result is True:
                integrity = True
                break

        self.log.info(f"Paddle signature integrity {'passed' if integrity else 'failed'}")
        return integrity


    def verify(self, signature_header: str, raw_body: str, secrets: list[Secret] | Secret) -> bool:
        """
        https://developer.paddle.com/webhooks/signature-verification
        Performs an integrity check on a Paddle webhook's signature against one or more Secrets
        Handling multiple Secrets is needed because of key rotation situations

        @param signature_header:    The Paddle-Signature header
        @param raw_body:            Raw body of the webhook request
        @param secrets:             One or more Paddle secret key(s): https://developer.paddle.com/webhooks/signature-verification#get-secret-key
        @return:                    True if any secret key passes verification success. Raises a ConnectionRefusedError if all secret keys fail verification
        """
        is_list   = type(secrets) is list
        key_count = 'multiple secret keys' if is_list else 'one secret key'
        self.log.info(f"Verifying Paddle signature integrity against {key_count}")

        timestamp, signature = PaddleSignature.parse(signature_header)

        if not is_list:
            return self.__do_verify(
                timestamp  = timestamp,
                signatures = signature[PaddleSignature().HASH_ALGORITHM_1],
                raw_body   = raw_body,
                secret_key = secrets,
            )

        for secret in secrets:
            verification_result = self.__do_verify(
                timestamp  = timestamp,
                signatures = signature[PaddleSignature().HASH_ALGORITHM_1],
                raw_body   = raw_body,
                secret_key = secret,
            )
            if verification_result is True:
                return True

        # If we got this far then none of the provided secrets passed verification
        raise ConnectionRefusedError(f"Paddle signature failed integrity check")
