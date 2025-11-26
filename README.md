# 🐉 CERBER ALFA 360

## Integrated Security System with ALFA Foundation

**Autor:** Karen Tonoyan © 2025 - ALFA Foundation

---

## 📋 Spis Treści

- [Opis](#opis)
- [Architektura](#architektura)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [API Reference](#api-reference)
- [Konfiguracja](#konfiguracja)
- [Integracja z ALFA 360](#integracja-z-alfa-360)

---

## 📖 Opis

**Cerber ALFA 360** to zaawansowany system bezpieczeństwa integrujący:

- **Symulowany Root** - bezpieczne środowisko testowe bez ryzyka uszkodzenia urządzenia
- **Whisper Perception** - warstwa 0 ALFA 360, filtrująca "hałas" i wykrywająca ukryte intencje
- **Samsung Knox Detection** - wykrywanie statusu Knox i typu roota
- **ALFA Bridge Sync** - synchronizacja z ekosystemem multi-AI
- **Interaktywna Konsola** - sterowanie chińskimi znakami (天干地支五行)
- **REST API** - zdalne zarządzanie przez HTTP
- **WebSocket** - real-time aktualizacje statusu

---

## 🏗️ Architektura

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CERBER ALFA 360                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │
│  │   Curses    │  │   REST API  │  │  WebSocket  │                │
│  │   Console   │  │  (FastAPI)  │  │   Server    │                │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                │
│         │                │                │                        │
│         └────────────────┼────────────────┘                        │
│                          │                                         │
│                   ┌──────▼──────┐                                  │
│                   │   CERBER    │                                  │
│                   │   ENGINE    │                                  │
│                   └──────┬──────┘                                  │
│                          │                                         │
│    ┌─────────────────────┼─────────────────────┐                  │
│    │                     │                     │                   │
│ ┌──▼──┐  ┌──────▼──────┐  ┌──▼──┐                                │
│ │KNOX │  │   WHISPER   │  │ALFA │                                │
│ │DETECT│  │ PERCEPTION │  │BRIDGE│                               │
│ └─────┘  └─────────────┘  └─────┘                                 │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              PROCESS THREADS (天干地支五行)                   │  │
│  ├─────────────────────────────────────────────────────────────┤  │
│  │ 甲 system_monitor    │ 乙 guardian_watchdog                 │  │
│  │ 丙 memory_scan       │ 丁 purge_emulator                    │  │
│  │ 戊 network_trace     │ 己 integrity_check                   │  │
│  │ 庚 knox_detector     │ 辛 alfa_bridge_sync                  │  │
│  │ 壬 whisper_filter    │ 癸 threat_analyzer                   │  │
│  │ 金 crypto_guardian   │ 木 log_aggregator                    │  │
│  │ 水 flow_controller   │ 火 alert_dispatcher                  │  │
│  │ 土 state_persistence │                                      │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Instalacja

### Wymagania

- Python 3.9+
- Opcjonalnie: FastAPI + Uvicorn (dla REST API)
- Opcjonalnie: websockets (dla WebSocket server)

### Instalacja podstawowa

```bash
# Klonowanie
git clone https://github.com/Karen86Tonoyan/cerber.git
cd cerber

# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie
python cerber_alfa360_core.py
```

### Instalacja z API

```bash
pip install fastapi uvicorn websockets
python cerber_alfa360_core.py --api
```

---

## 🚀 Użycie

### Tryb interaktywny (konsola curses)

```bash
python cerber_alfa360_core.py
```

**Sterowanie:**
- `甲-癸`, `金木水火土` - Toggle procesu (naciśnij symbol)
- `A` - Start all processes
- `S` - Stop all processes
- `Q` - Quit
- `R` - Refresh display
- `W` - Whisper stats popup
- `K` - Knox status popup

### Tryb API

```bash
# REST API na porcie 8360
python cerber_alfa360_core.py --api --api-port 8360

# WebSocket na porcie 8361
python cerber_alfa360_core.py --ws --ws-port 8361
```

### Tryb headless

```bash
python cerber_alfa360_core.py --headless
```

### Pobranie statusu

```bash
python cerber_alfa360_core.py --status
```

---

## 📡 API Reference

### Endpoints

| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET | `/` | Health check |
| GET | `/status` | Pełny status systemu |
| GET | `/processes` | Lista wszystkich procesów |
| GET | `/processes/{symbol}` | Status pojedynczego procesu |
| POST | `/processes/action` | Start/Stop/Toggle procesu |
| POST | `/processes/start-all` | Uruchom wszystkie |
| POST | `/processes/stop-all` | Zatrzymaj wszystkie |
| GET | `/knox` | Status Samsung Knox |
| GET | `/whisper` | Statystyki Whisper Perception |
| POST | `/whisper/normalize` | Normalizuj tekst przez Whisper |
| GET | `/logs/{process_name}` | Logi procesu |
| GET | `/alfa-bridge/queue` | Kolejka wiadomości ALFA Bridge |

### Przykłady

```bash
# Status
curl http://localhost:8360/status

# Toggle procesu 甲
curl -X POST http://localhost:8360/processes/action \
  -H "Content-Type: application/json" \
  -d '{"symbol": "甲", "action": "toggle"}'

# Whisper normalization
curl -X POST http://localhost:8360/whisper/normalize \
  -H "Content-Type: application/json" \
  -d '{"text": "URGENT!!! HELP NOW!!!"}'
```

---

## ⚙️ Konfiguracja

### Zmienne środowiskowe

| Zmienna | Opis | Domyślna |
|---------|------|----------|
| `CERBER_SIMROOT_PATH` | Ścieżka do katalogu fake root | Auto-detect |

### Argumenty CLI

```
--api              Włącz REST API server
--api-port PORT    Port dla API (default: 8360)
--ws               Włącz WebSocket server
--ws-port PORT     Port dla WebSocket (default: 8361)
--headless         Uruchom bez konsoli
--force-root PATH  Wymuś konkretny katalog root
--no-merge         Nie scalaj istniejących katalogów
--status           Wyświetl status i zakończ
```

---

## 🔗 Integracja z ALFA 360

### Whisper Perception

Cerber implementuje warstwę 0 ALFA 360 - **Whisper Perception**:

```python
from cerber_alfa360_core import WhisperPerception

whisper = WhisperPerception()
result = whisper.normalize_to_whisper("URGENT!!! Need help NOW!!!")

# Wynik:
# {
#   "original": "URGENT!!! Need help NOW!!!",
#   "normalized": "urgent! need help now!",
#   "semantic_value": 0.75,
#   "noise_detected": ["URGENT", "!!!"],
#   "threat_level": 0
# }
```

### ALFA Bridge Messages

```python
from cerber_alfa360_core import ALFABridgeMessage, ThreatLevel

msg = ALFABridgeMessage(
    source="cerber_engine",
    action="threat_detected",
    payload={"process": "threat_analyzer", "level": 3},
    threat_level=ThreatLevel.HIGH
)
```

### Knox Integration

```python
from cerber_alfa360_core import KnoxDetector

knox = KnoxDetector()
status = knox.get_knox_status()

# {
#   "is_android": True/False,
#   "root_type": "simulated|real|knox_protected",
#   "knox_version": "3.8" or None,
#   "knox_enabled": True/False,
#   "secure_folder_available": True/False,
#   "attestation_status": "locked|unlocked|unknown"
# }
```

---

## 📊 Dashboard

Otwórz `cerber_alfa360_dashboard.html` w przeglądarce dla graficznego interfejsu.

Dashboard oferuje:
- Real-time monitoring procesów
- Knox status panel
- Whisper perception stats
- Live logs terminal
- Process toggle controls

---

## 🔐 Bezpieczeństwo

**UWAGA:** Ten system jest **symulacją** i nie modyfikuje rzeczywistego systemu.

- Wszystkie operacje "root" są symulowane
- Logi zapisywane są w bezpiecznym katalogu (`/data/local/tmp/guardian_sim` lub `./guardian_sim`)
- Brak realnych zmian w systemie Android/Linux

---

## 📜 Licencja

**ALFA Creative License 1.0**

Wymagane cytowanie: Karen Tonoyan, ALFA Foundation

---

## 🤝 Kontakt

- **Autor:** Karen Tonoyan
- **Projekt:** ALFA Foundation
- **GitHub:** https://github.com/Karen86Tonoyan

---

*🐉 CERBER ALFA 360 - Zero Hallucination Security Protocol*
