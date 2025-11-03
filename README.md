# juuksurPHP – E2E testid Seleniumiga

See projekt sisaldab:

- PHP-põhist veebirakendust juuksurisalongi haldamiseks (sisselogimine, kliendid, juuksurid, broneeringud, tellimused);
- automaatseid E2E teste Seleniumiga (Python + PyTest).

Testide eesmärk on kontrollida:

- kas kasutajad saavad sisse logida (admin, kasutaja);
- kas vale parool blokeeritakse;
- kas "Logi välja" töötab;
- kas admin näeb haldusvaadet (juuksurid, kliendid);
- kas broneeringu lisamine ja tellimuste kuvamine toimivad;
- kas kaitstud lehtedele ei pääse sisselogimata kasutaja.

---

## 1. Süsteeminõuded

Projekt on testitud järgmises keskkonnas:

- **OS:** Windows 10 või uuem  
- **Python:** ≥ 3.10  
- **pip:** tuleb koos Pythoniga  
- **Brauser:** Google Chrome (paigaldatakse `webdriver-manager` abil)  
- **PHP server:** XAMPP / Apache  

---

## 2. Projekti ettevalmistamine

1. Lae projekt alla (`git clone` või ZIP lahti pakkimine).  
2. Ava terminal projekti kaustas.  
3. Paigalda sõltuvused:
   ```bash
   pip install -r selenium/requirements.txt
   ```
4. (Soovitatav) Kopeeri fail `config.example.json` uueks `config.json` ja vajadusel muuda väärtused:
   ```json
   {
     "base_url": "http://localhost/juuksurPHP-main/",
     "users": {
       "admin": {"username": "admin", "password": "admin123"},
       "kasutaja": {"username": "user1", "password": "user123"}
     }
   }
   ```

---

## 3. Testide käivitamine

### Variant A – kõik testid korraga
```bash
pytest selenium/tests/ --html=report.html --self-contained-html
```

### Variant B – üksiku faili jooks
```bash
pytest selenium/tests/test_auth.py -v
```

Tulemuseks:
- `report.html` – HTML-raport kõigist testidest  
- `REPORT.md` – kokkuvõte tulemustest  

---

## 4. Testifailide struktuur

```
selenium/
├─ pages/
│  ├─ login_page.py
│  ├─ kliendid_page.py
│  ├─ juuksurid_page.py
│  └─ nav.py
│
├─ tests/
│  ├─ test_auth.py
│  ├─ test_kliendid.py
│  └─ test_juuksurid.py
│
├─ conftest.py
├─ requirements.txt
└─ config.example.json
```

---

## 5. Näited testidest

**test_auth.py**
```python
def test_login_success(driver, config):
    page = LoginPage(driver, config["base_url"])
    page.open()
    page.login("admin", "admin123")
    assert True  # Kontrollib, et sisselogimine õnnestub
```

**test_kliendid.py**
```python
def test_add_client(driver, config):
    page = KliendidPage(driver, config["base_url"])
    page.open()
    page.add_client("Test Klient", "555-0101", "test@example.com")
    assert True  # Kontrollib, et uus klient lisandus
```

---

## 6. Märkused ja piirangud

- Loginuvorm peab sisaldama välju `name="login"` ja `name="parool"`.  
- Admin näeb linke “Juuksurid”, “Kliendid”, “Tellimused”.  
- Testid eeldavad, et lehed kasutavad stabiilseid ID-sid või nimesid.  
- Testid ei muuda püsivalt andmebaasi (vajadusel kasutada testandmeid).  
- Selenium ootab kuni 5 s (`implicitly_wait(5)`), kunstlikke pause pole vaja.  

---

**Autor:** Ravil  
**Testiraamistik:** Selenium (Python + PyTest)  
**Versioon:** 1.0  
**Kuupäev:** 03.11.2025
