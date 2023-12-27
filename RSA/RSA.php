<?php

class RSA
{
    private $publicKey;
    private $privateKey;

    public function __construct()
    {
        $config = [
            "digest_alg" => "sha512",
            "private_key_bits" => 4096,
            "private_key_type" => OPENSSL_KEYTYPE_RSA,
        ];

        $keyPair = openssl_pkey_new($config);
        openssl_pkey_export($keyPair, $privateKey);
        $this->privateKey = $privateKey;

        $publicKeyDetails = openssl_pkey_get_details($keyPair);
        $this->publicKey = $publicKeyDetails["key"];
    }

    public function getPublicKey()
    {
        return $this->publicKey;
    }

    public function getPrivateKey()
    {
        return $this->privateKey;
    }

    public function encrypt($data, $publicKey)
    {
        openssl_public_encrypt($data, $encrypted, $publicKey);
        return $encrypted;
    }

    public function decrypt($data, $privateKey)
    {
        openssl_private_decrypt($data, $decrypted, $privateKey);
        return $decrypted;
    }
}

?>
