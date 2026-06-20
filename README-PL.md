<div align="center">

# Alfa EOS

### Framework niezawodności, bezpieczeństwa i kontroli AI

**Autor:** Karen Tonoyan | **Wersja:** 1.0 | **Licencja:** CC BY-SA 4.0

---

**AI ma wspierać człowieka, a nie zastępować weryfikację, odpowiedzialność i kontrolę.**

</div>

---

## Czym jest Alfa EOS?

**Alfa EOS** to modularny framework do bezpieczniejszej pracy z systemami AI. Łączy walidację odpowiedzi, analizę niepewności, bramki bezpieczeństwa, audyt decyzji, nadzór człowieka oraz kontrolę wieloagentową.

System nie zakłada, że AI jest nieomylna. Zakłada odwrotnie: AI może zgadywać, pomijać kontekst, generować pozorną pewność i tworzyć błędne wnioski. ALFA ma ograniczać te ryzyka przez jawne procedury kontroli.

---

## Główna zasada

Jeżeli system nie wie, nie zgaduje.

```text
Jeżeli brakuje danych, kontekst jest niepełny albo ryzyko jest wysokie:
NIE wymyślaj.
Zapytaj, ostrzeż, zatrzymaj albo zablokuj.
```

---

## Moduły systemu

| Moduł               | Rola                                                              | Status                    |
| ------------------- | ----------------------------------------------------------------- | ------------------------- |
| **ALFA 360**        | Walidacja odpowiedzi, TDCM, Filtry Tonoyana, kontrola niepewności | Framework eksperymentalny |
| **CERBER**          | Bramka bezpieczeństwa i warstwa arbitrażu decyzji                 | Prototyp                  |
| **GUARDIAN**        | Monitoring stanu systemu i nadzór nad CERBEREM                    | Prototyp                  |
| **COLLECTIVE MIND** | Koncepcja pętli wieloagentowej i synchronizacji ocen              | Draft badawczy            |

---

## Architektura operacyjna

```text
Użytkownik / Organizacja
        |
        v
ALFA 360
Walidacja odpowiedzi + Filtry Tonoyana + TDCM
        |
        v
CERBER
Bramka bezpieczeństwa + arbitraż decyzji
        |
        v
GUARDIAN
Monitoring + nadzór stanu
        |
        v
COLLECTIVE MIND
Pętla sprzężenia zwrotnego między agentami
        |
        v
Człowiek w pętli decyzyjnej
PASS / WARN / CLARIFY / HOLD / BLOCK
```

---

## Decyzje systemowe

| Decyzja     | Znaczenie                | Kiedy używać                                                    |
| ----------- | ------------------------ | --------------------------------------------------------------- |
| **PASS**    | Można kontynuować        | Dane są wystarczające, ryzyko niskie                            |
| **WARN**    | Kontynuuj z ostrzeżeniem | Istnieje ryzyko lub niepewność, ale działanie jest dopuszczalne |
| **CLARIFY** | Poproś o doprecyzowanie  | Brakuje kontekstu albo intencja jest niejasna                   |
| **HOLD**    | Zatrzymaj do weryfikacji | Dane są zbyt słabe dla decyzji wysokiego znaczenia              |
| **BLOCK**   | Zablokuj                 | Działanie jest niebezpieczne, nielegalne albo nieuzasadnione    |

---

## 23 Filtry Tonoyana

Filtry Tonoyana to praktyczne pytania kontrolne, które pomagają oddzielić fakty od interpretacji, wykryć niepewność i uniknąć fałszywej pewności systemu AI.

### Warstwa 1: fundament

| #   | Filtr                         | Cel                                | Pytanie kontrolne                                   |
| --- | ----------------------------- | ---------------------------------- | --------------------------------------------------- |
| 2   | **Prawda**                    | Oddzielenie faktów od założeń      | Co jest faktem, a co interpretacją?                 |
| 17  | **Integralność AI**           | Zakaz fabrykowania odpowiedzi      | Czy odpowiedź jest oparta na danych, czy wymyślona? |
| 18  | **Weryfikacja źródeł**        | Kontrola dowodów                   | Jakie źródła potwierdzają odpowiedź?                |
| 21  | **Życie ludzkie**             | Priorytet bezpieczeństwa człowieka | Czy decyzja może wpłynąć na realną osobę?           |
| 22  | **Partnerstwo intelektualne** | Konstruktywna krytyka              | Czy system pomaga myśleć, czy tylko potakuje?       |
| 23  | **Dowody i argumentacja**     | Uzasadnienie decyzji               | Gdzie są dowody i jak wygląda tok rozumowania?      |

### Warstwa 2: decyzje złożone

| #   | Filtr                       | Cel                         | Pytanie kontrolne                         |
| --- | --------------------------- | --------------------------- | ----------------------------------------- |
| 1   | **Kontekst**                | Pełny obraz sytuacji        | Jakiego kontekstu brakuje?                |
| 3   | **Perspektywa**             | Analiza z wielu stron       | Jak wygląda to z innej perspektywy?       |
| 4   | **Konsekwencje**            | Skutki dalszego rzędu       | Co może stać się później?                 |
| 6   | **Zasoby**                  | Realna wykonalność          | Co mamy, czego brakuje?                   |
| 7   | **Czas**                    | Dobór momentu               | Czy to jest właściwy moment na działanie? |
| 8   | **Ryzyko**                  | Wykrywanie zagrożeń         | Co może pójść źle?                        |
| 12  | **Falsyfikacja**            | Szukanie błędów             | Co udowodniłoby, że się mylimy?           |
| 13  | **Alternatywy**             | Unikanie tunelu decyzyjnego | Jakie są inne opcje?                      |
| 16  | **Meta**                    | Ocena metody                | Czy metoda analizy jest poprawna?         |
| 19  | **Transparentność procesu** | Jawność działań             | Czy proces można odtworzyć i sprawdzić?   |
| 20  | **Komunikacja niepewności** | Unikanie fałszywej pewności | Jaki jest poziom pewności i dlaczego?     |

### Warstwa 3: domena i wartości

| #   | Filtr                      | Cel                                | Pytanie kontrolne                                 |
| --- | -------------------------- | ---------------------------------- | ------------------------------------------------- |
| 5   | **Emocje**                 | Oddzielenie emocji od danych       | Co czuję, a co wiem?                              |
| 9   | **Wartości**               | Spójność z zasadami                | Czy decyzja jest zgodna z wartościami projektu?   |
| 10  | **Prostota**               | Najprostsze działające rozwiązanie | Jakie jest najprostsze rozwiązanie, które działa? |
| 11  | **Zależności**             | Łańcuch przyczynowy                | Co od czego zależy?                               |
| 14  | **Integralność publiczna** | Obrona decyzji                     | Czy da się to uczciwie obronić publicznie?        |
| 15  | **Skalowanie**             | Test skali                         | Co stanie się przy 10x, 100x, 1000x?              |

---

## Protokół redukcji halucynacji

ALFA nie obiecuje dosłownego „zera halucynacji”. Celem jest redukcja ryzyka błędnych odpowiedzi i wymuszanie jawnej niepewności.

Proces walidacji:

1. Zbierz pytanie, kontekst i ograniczenia.
2. Oddziel fakty od założeń.
3. Zastosuj Filtry Tonoyana.
4. Oceń ryzyko i poziom pewności.
5. Wybierz decyzję: PASS, WARN, CLARIFY, HOLD albo BLOCK.
6. Zapisz uzasadnienie w śladzie audytowym.

---

## Status metryk i dowodów

Wszystkie liczby dotyczące redukcji halucynacji, wzrostu zgodności modeli albo poziomu pewności powinny być traktowane jako eksperymentalne, dopóki nie istnieje publiczny benchmark, dataset, opis protokołu testowego lub powtarzalna ewaluacja.

Bez benchmarku należy używać ostrożnego języka:

- „system zaprojektowany do redukcji halucynacji”
- „framework wspierający walidację odpowiedzi”
- „warstwa kontroli niepewności”
- „human-in-the-loop safety framework”

Nie należy traktować hasła „zero halucynacji” jako gwarancji technicznej.

---

## CERBER

**CERBER** to warstwa bezpieczeństwa i arbitrażu decyzji. Jego zadaniem jest ocena, czy dana odpowiedź, akcja albo decyzja może przejść dalej.

Przykładowe funkcje:

- wykrywanie ryzyka,
- blokowanie niebezpiecznych akcji,
- wymuszanie doprecyzowania,
- sprawdzanie zgodności z regułami,
- przekazywanie decyzji do człowieka, gdy ryzyko jest wysokie.

Werdykty CERBERA:

| Werdykt      | Znaczenie                      |
| ------------ | ------------------------------ |
| **APPROVE**  | Działanie dopuszczalne         |
| **QUESTION** | Wymagana dodatkowa weryfikacja |
| **WARN**     | Możliwe ryzyko                 |
| **BLOCK**    | Działanie niedopuszczalne      |
| **ESCALATE** | Przekaż do człowieka           |

---

## GUARDIAN

**GUARDIAN** to warstwa monitoringu. Nie zastępuje CERBERA, tylko nadzoruje jego stan i spójność działania.

Przykładowe funkcje:

- obserwacja stanu systemu,
- wykrywanie niespójności,
- sygnalizowanie awarii logiki,
- nadzór nad pętlą decyzyjną,
- wsparcie audytu.

---

## COLLECTIVE MIND

**COLLECTIVE MIND** to warstwa badawcza dla systemów wieloagentowych. Jej zadaniem jest porównywanie ocen, wykrywanie rozbieżności i wspieranie decyzji przez pętlę sprzężenia zwrotnego.

Nie oznacza to literalnej świadomości AI. W tym repo oznacza to operacyjny model współpracy wielu instancji, agentów lub modułów walidacyjnych.

---

## Zastosowania

Alfa EOS może być rozwijany w kierunku:

- audytów bezpieczeństwa AI,
- walidacji odpowiedzi modeli językowych,
- kontroli prompt injection,
- nadzoru nad agentami AI,
- systemów human-in-the-loop,
- edukacji z zakresu bezpiecznego użycia AI,
- dokumentowania decyzji i śladów audytowych,
- wdrożeń AI w małych firmach i organizacjach.

---

## Struktura repozytorium

```text
ALFA-ECOSYSTEM-COMPLETE/
|
|-- README.md                    # Główna dokumentacja ekosystemu
|-- LICENSE.md                   # Licencja CC BY-SA 4.0
|
|-- ALFA-360/                    # Walidacja odpowiedzi i Filtry Tonoyana
|   |-- README.md
|   |-- Manifesto-PL.md
|   |-- CHECKLIST.md
|   |-- INSTRUKCJA.md
|   |-- docs/
|   `-- assets/
|
|-- CERBER/                      # Bramka bezpieczeństwa AI
|   |-- README.md
|   `-- src/
|
|-- GUARDIAN/                    # Monitoring systemu
|   |-- README.md
|   `-- src/
|
`-- COLLECTIVE-MIND/             # Warstwa wieloagentowa
    |-- README.md
    `-- src/
```

---

## Szybki start

```bash
git clone https://github.com/Karen86Tonoyan/-ALFA-360-Open-Manifesto-.git
cd -ALFA-360-Open-Manifesto-/ALFA-ECOSYSTEM-COMPLETE

python GUARDIAN/src/core/guardian.py
python COLLECTIVE-MIND/src/collective_mind.py
```

---

## Licencja

**Creative Commons BY-SA 4.0** z wymaganym przypisaniem autorstwa:

```text
Alfa EOS Framework by Karen Tonoyan
```

---

## Autor

**Karen Tonoyan**

Twórca koncepcji ALFA, CERBER, GUARDIAN, ALFA Bridge, Filtrów Tonoyana oraz powiązanych metod pracy nad bezpieczeństwem AI.

---

<div align="center">

## Alfa EOS

**Niezawodność AI. Kontrola człowieka. Bezpieczeństwo przez projekt.**

**© 2025 Karen Tonoyan — ALFA Foundation**

</div>
