<?php

require_once 'RSA.php';

// Membuat objek RSA
$rsa = new RSA();

// Menyimpan kunci publik dan privat ke file
file_put_contents('public_key.pem', $rsa->getPublicKey());
file_put_contents('private_key.pem', $rsa->getPrivateKey());

// Membaca teks dari file input.txt
$inputText = file_get_contents('input.txt');

// Melakukan enkripsi
$encryptedData = $rsa->encrypt($inputText, $rsa->getPublicKey());
file_put_contents('encrypted_data.bin', $encryptedData);

// Melakukan dekripsi
$decryptedData = $rsa->decrypt($encryptedData, $rsa->getPrivateKey());
file_put_contents('decrypted_data.txt', $decryptedData);

?>
