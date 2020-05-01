class Miner:

    def __init__(self, name_in, initial_value_in):
        """
            it contain
            * empty list of received transactions
            * block_chain
            * name
            * initial_value
            * public key
            * private key
        """
        # Todo
        pass

    def proof_of_work(self, block):
        """
            Function that tries different values of the nonce to get a hash
            that satisfies our difficulty criteria.
            return computed hash
        """
        # Todo
        pass

    def bft(self, block):
        """
            Function that get votes from all members on block validity
            return valid or not (majority vote)
        """
        # Todo
        pass

    def add_new_transaction(self, transaction):
        """
            add received transaction to the list of received transactions
        """
        # Todo
        pass

    def is_valid_proof(self, block, block_hash):
        """
            * Check if block_hash is valid hash of block and satisfies the difficulty criteria.
            * check if block contain threshold transactions
            return true or false
        """
        # Todo
        pass

    def check_chain_validity(self, chain):
        """
            A helper method to check if the entire blockchain is valid.
            Iterate through every block and check if it is valid
            return true if valid or false if not
        """
        # Todo
        pass

    def mine(self):
        """
            This function serves as an interface to add the pending
            transactions to the blockchain by adding them to the block
            and figuring out Proof Of Work or BFT.
            return true if done (pow or bft) or false if not
        """
        # Todo
        pass

    # Transaction Verification Methods
    def sign_utxo(self, recipient_in, utxo_in):
        """
            From Satoshi's White Paper:
                - Each owner transfers the coin to the next by digitally signing
                a hash of the previous transaction and the public key of the next owner
            * create (utxo, receipent) to sign
            * sign
        """
        # Todo
        pass

    def verify_utxo(self, sender_in, utxo_in):
        """
            From Satoshi's White Paper:
            - A payee can verify the signatures to verify the chain of ownership.
            * create (utxo, receipent) to vertify
            *  verify using public key
            return true if valid signature or false if not
        """
        # TODO
        pass
