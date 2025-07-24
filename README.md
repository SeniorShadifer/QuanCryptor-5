# QuanCryptor-5
Client-server messenger on Python with post-quantum encryption. Uses PyWebview as client GUI


## Description

### Post-quantum algorithms
Uses AES and McEliese to hybrid and symmetric encryption. The module loader allows you to add support for other algorithms. The "cryptography" library version 44.0.2 provides cryptographic functions.

### Module loader
The module loader, which is built into the client and server, allows you to use third-party themes, styles, algorithms, and other features.

### Client GUI
The graphical web user interface is provided by the "pywebview" library. No frameworks are used for the interface.

### Client-server architecture
The application has a client-server architecture. The servers store accounts, chats, and messages, which are encrypted on the client side. Hybrid and symmetric encryption can be used.

To connect to the server, you need to have the hash of its certificate. The certificate contains information about the algorithms used, the public key (if asymmetric encryption is used), and other data.
