# 📘 INSTRUKCJA PUBLIKACJI — ALFA 360

**Autor:** Karen Tonoyan  
**Cel:** Przewodnik krok po kroku do publikacji i zarządzania repozytorium ALFA 360

---

## 🚀 1. Szybki Start (5 minut)

### Krok 1: Utwórz repozytorium

1. Wejdź na: https://github.com/new
2. Wypełnij:
   - **Nazwa:** `ALFA-360-Open-Manifesto`
   - **Opis:** `Framework for Zero-Hallucination AI & Strategic Thinking by Karen Tonoyan`
   - **Public:** ✓
   - **Add README:** ✓
3. Kliknij **Create repository**

### Krok 2: Dodaj pliki

Upload wszystkich plików z tego pakietu:

```
README.md
Manifesto-PL.md
LICENSE.md
CHECKLIST.md
INSTRUKCJA.md
_config.yml
.gitignore
docs/
assets/
```

### Krok 3: Aktywuj GitHub Pages

1. Wejdź w repo → **Settings**
2. Z menu po lewej wybierz **Pages**
3. Ustaw:
   - **Source:** `main`
   - **Folder:** `/ (root)`
4. Kliknij **Save**

Po 1–3 minutach strona będzie dostępna pod:
```
https://karen86tonoyan.github.io/-ALFA-360-Open-Manifesto-/
```

---

## 📁 2. Struktura Plików

### Pliki główne (root)

| Plik | Funkcja |
|------|---------|
| `README.md` | Strona główna projektu (EN) |
| `Manifesto-PL.md` | Pełny manifest (PL) |
| `LICENSE.md` | Licencja z obowiązkiem cytowania |
| `CHECKLIST.md` | Lista kontrolna jakości |
| `INSTRUKCJA.md` | Ten przewodnik |
| `_config.yml` | Konfiguracja Jekyll/GitHub Pages |
| `.gitignore` | Ignorowane pliki |

### Folder /docs

| Plik | Zawartość |
|------|-----------|
| `filters.md` | 23 Filtry Tonoyona |
| `architecture.md` | Architektura systemu |
| `validation.md` | Protokół walidacji |
| `anti-patterns.md` | Błędy i anty-wzorce |
| `case-studies.md` | Studia przypadków |
| `philosophy.md` | Filozofia ALFA |

### Folder /assets

| Ścieżka | Zawartość |
|---------|-----------|
| `assets/css/style.scss` | Styl czarno-złoty |
| `assets/images/` | Grafiki i banery |

---

## 🎨 3. Wdrożenie Stylu ALFA 360

### Motyw czarno-złoty

Plik `_config.yml` konfiguruje motyw `minima` z customowym CSS.

Plik `assets/css/style.scss` zawiera:
- Czarne tło (#080808)
- Złote akcenty (#C5A059)
- Typografię minimalistyczną
- Wysoki kontrast

### Weryfikacja stylu

Po aktywacji GitHub Pages sprawdź:
1. Tło jest czarne
2. Nagłówki są złote
3. Linki działają
4. Strona jest czytelna na telefonie

---

## 🔧 4. Aktualizacja Zawartości

### Przez interfejs GitHub (prosty sposób)

1. Wejdź w plik, który chcesz edytować
2. Kliknij ikonę ołówka (Edit)
3. Wprowadź zmiany
4. Na dole wpisz opis zmian
5. Kliknij **Commit changes**

### Przez Git (zaawansowany sposób)

```bash
# Sklonuj repo
git clone https://github.com/Karen86Tonoyan/-ALFA-360-Open-Manifesto-.git

# Wejdź do folderu
cd -ALFA-360-Open-Manifesto-

# Wprowadź zmiany w plikach

# Dodaj zmiany
git add .

# Zatwierdź
git commit -m "Opis zmian"

# Wyślij na GitHub
git push origin main
```

---

## 🔒 5. Bezpieczeństwo

### Tokeny GitHub

⚠️ **NIGDY nie udostępniaj tokenów publicznie!**

Jeśli token wyciekł:
1. Wejdź: https://github.com/settings/tokens
2. Znajdź token → **Revoke** lub **Delete**
3. Wygeneruj nowy token

### Dobre praktyki

- Używaj tokenów z minimalnymi uprawnieniami
- Ustaw datę wygaśnięcia
- Nie wklejaj tokenów w kod ani w chat

---

## 📊 6. Monitorowanie

### GitHub Insights

W repo → **Insights** znajdziesz:
- Statystyki ruchu
- Klony i widoki
- Forks
- Contributors

### Google Analytics (opcjonalnie)

W `_config.yml` możesz dodać:
```yaml
google_analytics: UA-XXXXXXXXX-X
```

---

## 🌐 7. SEO i Widoczność

### Topics (tagi)

Dodaj topics w Settings → General:
- `ALFA360`
- `Tonoyan`
- `zero-hallucination`
- `AI-safety`
- `strategic-thinking`
- `manifesto`

### Opis repo

Uzupełnij opis:
```
Framework for Zero-Hallucination AI & Strategic Thinking by Karen Tonoyan
```

### Link do strony

W About (prawy panel) dodaj link do GitHub Pages.

---

## 🔄 8. Workflow Aktualizacji

### Mała zmiana (literówka, poprawka)

1. Edytuj bezpośrednio na GitHub
2. Commit z opisem

### Duża zmiana (nowa sekcja, restrukturyzacja)

1. Utwórz branch: `git checkout -b feature/nowa-funkcja`
2. Wprowadź zmiany
3. Przetestuj lokalnie
4. Merge do main

### Nowa wersja

1. Zaktualizuj numer wersji w README i Manifesto
2. Dodaj wpis do historii wersji
3. Utwórz Release na GitHub

---

## ❓ 9. Rozwiązywanie Problemów

### Problem: GitHub Pages nie działa

**Rozwiązanie:**
1. Sprawdź Settings → Pages → czy Source = main
2. Poczekaj 2-3 minuty
3. Sprawdź czy `_config.yml` jest poprawny

### Problem: Styl się nie ładuje

**Rozwiązanie:**
1. Sprawdź ścieżkę do `style.scss`
2. Upewnij się że plik zaczyna się od `---`
3. Wyczyść cache przeglądarki (Ctrl+F5)

### Problem: Błąd 404

**Rozwiązanie:**
1. Sprawdź nazwy plików (wielkie/małe litery)
2. Sprawdź linki wewnętrzne
3. Upewnij się że plik istnieje

### Problem: Git lockfile

**Rozwiązanie:**
```bash
rm -f .git/index.lock
```

---

## 📞 10. Wsparcie

### Dokumentacja

- Ten plik: `INSTRUKCJA.md`
- Checklista: `CHECKLIST.md`
- Licencja: `LICENSE.md`

### Kontakt

- **Autor:** Karen Tonoyan
- **Organizacja:** ALFA Foundation
- **Repo:** https://github.com/Karen86Tonoyan/-ALFA-360-Open-Manifesto-

---

## ✅ Checklist Przed Publikacją

- [ ] Wszystkie pliki dodane
- [ ] GitHub Pages aktywowane
- [ ] Styl działa poprawnie
- [ ] Linki wewnętrzne działają
- [ ] Topics dodane
- [ ] Opis repo uzupełniony
- [ ] Licencja widoczna

---

**Gotowe do wdrożenia!**

*„Zero halucynacji. Zero chaosu. Zero kompromisów."*

— Karen Tonoyan, ALFA Foundation
