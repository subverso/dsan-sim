import hashlib
import time
from typing import List, Dict
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ed25519

class DSANAgent:
    """
    Agente soberano DSAN com identidade criptográfica.
    - Chaves Ed25519
    - Logs hash-encadeados (auditáveis)
    - Verificação de mensagens assinadas
    """
    
    def __init__(self, agent_id: str):
        self.id = agent_id
        # Gera par de chaves (simula totem)
        self.private_key = ed25519.Ed25519PrivateKey.generate()
        self.public_key_bytes = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        self.inbox: List[Dict] = []
        self.local_log: List[Dict] = []
        self.state_hash = b""
        
    def sign_message(self, msg: Dict) -> bytes:
        """Assina mensagem (simula totem assinando)"""
        msg_bytes = str(msg).encode()
        return self.private_key.sign(msg_bytes)
    
    def verify_message(self, msg: Dict, signature: bytes, sender_pubkey: bytes) -> bool:
        """Verifica assinatura (anti-spoofing)"""
        try:
            sender_key = ed25519.Ed25519PublicKey.from_public_bytes(sender_pubkey)
            msg_bytes = str(msg).encode()
            sender_key.verify(signature, msg_bytes)
            return True
        except:
            return False
    
    def receive(self, msg: Dict, signature: bytes, sender_id: str, sender_pubkey: bytes) -> bool:
        """Recebe msg com verificação"""
        if not self.verify_message(msg, signature, sender_pubkey):
            self.log_event("REJECTED_INVALID_SIG", sender_id)
            return False
        
        self.inbox.append({
            "timestamp": time.time(),
            "sender": sender_id,
            "msg": msg
        })
        self.log_event("MSG_RECEIVED", sender_id, msg.get("type"))
        return True
    
    def log_event(self, event_type: str, *args):
        """Log append-only com hash chain"""
        event = {
            "timestamp": time.time(),
            "agent": self.id,
            "type": event_type,
            "args": list(args)
        }
        event_hash = hashlib.sha256(str(event).encode()).digest()
        self.local_log.append({"event": event, "hash": event_hash.hex()})
        self.state_hash = hashlib.sha256(self.state_hash + event_hash).digest()
    
    def get_state_proof(self) -> Dict:
        """Prova auditável de estado"""
        return {
            "agent_id": self.id,
            "state_hash": self.state_hash.hex(),
            "log_length": len(self.local_log)
        }
