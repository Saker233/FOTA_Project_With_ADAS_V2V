
```markdown
# File Processing Toolkit

This part of the project provides a set of Python scripts for file encryption, decryption, signature generation, and verification, as well as file concatenation and cleanup.

## Usage

### Setting Up Environment Variables

Before running the scripts, ensure you have set up the necessary environment variables for encryption, decryption, and signature generation. You can store these keys in a file named `secret_keys.env` using the following format:

```plaintext
export key="your_encryption_key" #signature secret key
export d="your_decryption_key"   # private key
export n="your_modulus_value"    # modulus
```

Ensure the file permissions for `secret_keys.env` are restricted to your user by running:

```bash
chmod 600 secret_keys.env
```

To automatically load these environment variables every time you open a terminal session, add the following line to your `.bashrc` file:

```bash
source /path/to/secret_keys.env
```

### Running the Scripts

1. **OEM_encryption.py**: Encrypts a file using RSA encryption.

    ```bash
    python OEM_encryption.py /path/to/file.hex
    ```

2. **OEM_signature.py**: Generates a cryptographic signature for a file using HMAC-SHA256.

    ```bash
    python OEM_signature.py /path/to/file.hex
    ```

3. **concatenation_script.py**: Concatenates two files with a delimiter.

    ```bash
    python concatenation_script.py /path/to/first_file /path/to/second_file
    ```

4. **RPI_scenario.py**: Executes a scenario involving file separation, decryption, digest creation, signature verification, and file cleanup.

    ```bash
    python RPI_scenario.py /path/to/concatenated_file.hex /path/to/old_digest.hex /path/to/new_digest.hex
    ```
