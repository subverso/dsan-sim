import random
import time
from typing import List
from dsan_sim.agent import DSANAgent

class DSANSimulator:
    """
    Simulador de rede DSAN.
    Testa: identidade, mensagens assinadas, falhas de rede.
    """
    
    def __init__(self, agents: List[DSANAgent], network_loss: float = 0.1):
        self.agents = {agent.id: agent for agent in agents}
        self.network_loss = network_loss  # % mensagens perdidas
        self.time_step = 0
    
    def send_message(self, sender_id: str, receiver_id: str, msg: dict):
        """Envia msg com perda de rede simulada"""
        if random.random() < self.network_loss:
            print(f"💥 MSG DROPPADA: {sender_id} → {receiver_id}")
            return
        
        sender = self.agents[sender_id]
        signature = sender.sign_message(msg)
        receiver = self.agents[receiver_id]
        
        if receiver.receive(msg, signature, sender_id, sender.public_key_bytes):
            print(f"✅ {sender_id} → {receiver_id}: {msg.get('type', 'msg')}")
        else:
            print(f"❌ {sender_id} rejeitada por {receiver_id}")
    
    def run(self, steps: int = 10):
        """Executa simulação"""
        print(f"🌐 DSAN-Sim iniciando {len(self.agents)} agentes")
        for step in range(steps):
            self.time_step = step
            
            # Exemplo: agente1 manda HELLO para todos
            if 'agent1' in self.agents:
                for receiver_id in self.agents:
                    if receiver_id != 'agent1':
                        self.send_message(
                            'agent1', 
                            receiver_id, 
                            {"type": "HELLO", "step": step, "content": "DSAN test"}
                        )
            
            time.sleep(0.1)  # Simula tempo real
        
        # Relatório final
        print("\n📊 Estado final:")
        for agent_id, agent in self.agents.items():
            proof = agent.get_state_proof()
            print(f"  {agent_id}: {len(agent.inbox)} msgs, hash={proof['state_hash'][:8]}"
