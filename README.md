# Servizio Newsletter Compleanni

> API Django per gestire un servizio interno di newsletter che notifica i compleanni dei dipendenti e conserva lo storico degli invii.

## Stato del progetto

Funzionalità incluse:

- Gestione anagrafica dipendenti tramite API REST con full CRUD;
- Consultazione sedi e team in modalità solo lettura;
- Invio manuale della newsletter compleanni ai festeggiati e ai colleghi;
- Generazione dei template email in modalità custom, con override del template standard;
- Tracciamento degli invii effettuati;
- Backend email mock su console;
- Dati di esempio creati tramite management command (`populate_database`);
- Collection Postman inclusa nel repository;
- Docker Compose file per testare le API via Docker.

## Come iniziare

Il progetto può essere avviato tramite Docker Compose oppure in locale con Python.

L'applicazione espone API REST utilizzabili da Postman o con altri strumenti.

## Dipendenze

Le dipendenze Python nello specifico sono definite in `requirements.txt`.

## Installazione

### Avvio con Docker Compose (CONSIGLIATO)

```bash
docker compose up --build
```

Il container esegue automaticamente:

```bash
python3 manage.py migrate
python3 manage.py populate_database
python3 manage.py runserver 0.0.0.0:8000
```

### Avvio locale

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py populate_database
python manage.py runserver
```

Se il database è già popolato, il comando `populate_database` evita di duplicare sedi e team già presenti.


## Descrizione modello dati scelto

Il modello dati è stato organizzato separando l’anagrafica aziendale dalla parte relativa all’invio e al tracciamento delle notifiche. Si è fatto ricorso a Model che si appoggiano a ModelViewSet per gestire CRUD.

- `Branch`: Rappresenta una sede aziendale, identificata da nazione e città;
- `Team`: rappresenta un team aziendale collegato a una specifica sede;
- `Employee`: rappresenta il dipendente, con dati anagrafici, email, data di nascita, stato attivo/non attivo e team di appartenenza;
- `NotificationRun`: rappresenta una singola esecuzione del processo di invio newsletter;
- `Template`: contiene oggetto e corpo dell’email generata per uno specifico destinatario;
- `EmailLog`: conserva lo storico delle email inviate, collegando template e run di invio.

## Utilizzo

Dopo l'avvio, le API sono disponibili su:

```bash
http://127.0.0.1:8000/
```

Nel repository è presente anche la collection Postman:

```bash
django_newsletter.postman_collection.json
```

## Esempi di chiamate API (curl)

### Consultazione dipendenti

```bash
curl -X GET http://127.0.0.1:8000/employees/
```

### Consultazione sedi

```bash
curl -X GET http://127.0.0.1:8000/branches/
```

### Consultazione team

```bash
curl -X GET http://127.0.0.1:8000/teams/
```

### Invio manuale newsletter compleanni

```bash
curl -X POST http://127.0.0.1:8000/notification_runs/send_bday_emails/
```

### Consultazione storico invii

```bash
curl -X GET http://127.0.0.1:8000/notification_runs/
```

### Consultazione log email

```bash
curl -X GET http://127.0.0.1:8000/email_logs/
```

## Funzionalità

Il progetto usa il backend email console di Django:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Non servono credenziali SMTP reali. Quando viene chiamato il trigger manuale, le email vengono stampate nello standard output del processo Django.

## Regole applicate

- Di default, vengono considerati solo i dipendenti con stato `active = true`;
- I dipendenti del team `Administrative` sono esclusi di default dall'invio, in quanto responsabili loro stessi dell'invio;
- I dipendenti che compiono gli anni oggi ricevono un'email dedicata di auguri;
- Gli altri dipendenti ricevono un'email informativa con l'elenco dei festeggiati e un invito a contattarli;
- Il template utilizza i dati dei dipendenti di default;
- È possibile modificare il messaggio inviato tramite parametri custom nella chiamata di invio.
    Infatti, si può fare l'override del messaggio ricevuto da tutti esempi (es: 'custom_subject_no_bday' per diverso oggetto).
    Si rimanda all'esempio presente nella collection Postman.

## Limiti e sviluppi futuri

Possibili miglioramenti:

- Introdurre un vero scheduler giornaliero per l'invio automatico delle e-mail;
- Creare un sistema di gestione e-mail completo, con utenti che possono mandare certi tipi di e-mail se autorizzati;
- Aggiungere filtri per sede, team e stato del dipendente;
- Distinguere oltre che tra stato "attivo" e "non attivo" tra ferie, maternità, licenziamento, dimissioni, ecc.;
- Aggiungere autenticazione e autorizzazioni;
- Sostituire SQLite con un server database in ambiente di produzione;
- Aggiungere logging applicativo strutturato;
- Aggiungere documentazione OpenAPI/Swagger.