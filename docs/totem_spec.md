# DSAN Totem v0.1 – Hardwallet Soberana

## Hardware mínimo
Microcontrolador: ESP32-S3 (WiFi/BLE, R$30)
HSM: ATECC608B (FIPS, R$10)
Interface: PIN de 6 dígitos + NFC
Backup: Semente BIP39 de 24 palavras
Firmware: AGPL3 open source

## Fabricantes certificados (futuro)
✅ Ledger/Trezor DSAN Edition
✅ Hardware aberto (Seeed/XIAO)
✅ Empresas BR (certificado Anatel)

## Fluxo de segurança
Compre totem certificado DSAN

PIN inicial → semente de gera (salve papel)

Totem cria: DID + chaves agentes + AES memória

Semente de backup = total

Falha no totem? Semente → novo totem

## Propriedades
🔒 Chaves NUNCA expostas
🛡️ PIN + 3 tentativas = lockout
💥 Autodestruição (opcional)
🔄 Recuperação: seed + hardware novo
📱 App: aprovação de ações remotas

## Mock no simulador
Veja `totem_mock.py` (futuro).

**Convocação**: Fabricantes, firmware devs → colaborem.
