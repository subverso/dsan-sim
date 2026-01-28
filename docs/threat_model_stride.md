# DSAN Threat Model v0.1 – STRIDE

## Superfícies de ataque
- **Agente** (identidade, chaves)
- **Rede** (mensagens P2P)
- **Totem** (hardware mock)
- **Logs** (auditabilidade)

## Tabela STRIDE

| Categoria | ID | Ameaça DSAN | Mitigação | Status |
|-----------|----|-------------|-----------|--------|
| **Spoofing** | S1 | Fake identity | Chaves Ed25519 + verify | ✅ |
| **Spoofing** | S2 | Sybil attack | Prova de participação | 🔄 |
| **Tampering** | T1 | Msg alterada | Sign E2E | ✅ |
| **Repudiation** | R1 | Nega envio | Logs hash-chain | ✅ |
| **Disclosure** | I1 | Chaves vazadas | Totem mock (futuro HSM) | 🔄 |
| **DoS** | D1 | Flooding | Rate limiting simulado | ✅ |
| **Elevation** | E1 | Escala privilégio | Regras explícitas | 🔄 |

## Testes implementados
- `examples/basic_network.py` → S1, T1, D1
- Futuro: `sybil_attack.py` → S2

**Encontre falhas. Abra Issues.**
