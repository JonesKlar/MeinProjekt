# Dokumentation

Erstelle eine README-Datei im Wurzelverzeichnis deines lokalen Repositories.

Dokumentiere in der README-Datei die folgenden Punkte:

- [Erstellen eines ssh-Schlüsselpaares](#erstellen-eines-ssh-schlüsselpaares)
  - [SSH-Schlüssel generieren](#ssh-schlüssel-generieren)
  - [Generierte Schlüssel](#generierte-schlüssel)
  - [SSH-Dienst starten](#ssh-dienst-starten)
- [Einrichten des GitHub-Repositorys "MeinProjekt"](#einrichten-des-github-repositorys-meinprojekt)
  - [Public key registrieren](#public-key-registrieren)
  - [Neues Repository "MeinProjekt" erstellen](#neues-repository-meinprojekt-erstellen)
- [Lokales Klonen des Repositorys, Konfiguration von Git, Erstellen der initialen Commits](#lokales-klonen-des-repositorys-konfiguration-von-git-erstellen-der-initialen-commits)
- [Erstellen des "feature"-Branches](#erstellen-des-feature-branches)
- [Mergen des "feature"-Branches in den "main"-Branch](#mergen-des-feature-branches-in-den-main-branch)
- [Übertragen der Änderungen in das Remote repository](#übertragen-der-änderungen-in-das-remote-repository)

---

## Erstellen eines ssh-Schlüsselpaares

### SSH-Schlüssel generieren   

In der Git Bash Konsole folgendes Kommando eingeben (Default Pfad oder eigenen Pfad nutzen).
E-Mail muss die E-Mail-Adresse des Github Kontos sein!

    ssh-keygen -t ed25519 -C "your_github_account_email@example.com"

<img src="screens/ssh-console.png" width="600">

### Generierte Schlüssel:

<img src="screens/ssh-private-public-key.png" width="400">

Die Datei ".pub" ist der öffentliche Schlüssel.
Öffne diesen mit Notepad und notiere dir den gesamten Inhalt. Dieser wird später in Github registriert.

### SSH-Dienst starten

Start den lokalen ssh service. Öffne dazu die Powershell Konsole mit Admin Rechten:

<img src="screens/ssh-agent-start.png" width="500">

In einer einfachen Windows Shell ohne Adminrechte folgeenden befehl ausführen, um den privaten `ssh` Schlüssel dem lokalen ssh Agent hinzuzufügen

<img src="screens/ssh-private-key-agent.png" width="600">


##  Einrichten des GitHub-Repositorys "MeinProjekt"

### Public key registrieren

Auf github.com mit E-Mail Adresse einloggen/registrieren. Die E-Mail muss die gleiche sein, mit der vorher die `ssh` Schlüssel generiert worden sind.

Öffentlichen `ssh` Schlüssel im Github Account eintragen, folgende Schritte:

1. www.github.com aufrufen
2. Auf eigenes Profilbild klicken und dann auf `Settings`
3. Im Bereich `Access` auf `SSH und GPG keys` klicken
4. Zuvor generierten öffentlichen Schlüssel eintragen und mit `Add SSH key` bestätigen
 
<img src="screens/ssh-github.com.png" width="400">

Registrierter `public ssh key`

<img src="screens/ssh-github-result.png" width="400">


### Neues Repository "MeinProjekt" erstellen

Gehe zu GitHub (www.github.com) und melde dich mit deinem Benutzerkonto an. Falls du noch kein Konto hast, registriere dich kostenlos.

Nach dem Login klicke auf "+ New" (oben rechts) und erstelle ein neues leeres Repository mit dem Namen "MeinProjekt".

Notiere dir die URL des erstellten Repositories, sie wird später benötigt.


<img src="screens/new-repo.png" height="200">

Den Projektnamen eingeben und mit "Create repository bestätigen"

<img src="screens/new-repo-1.png" width="400">

Auf der Projektseite die hier angezeigte git Projekturl notieren, die wir zum späteren Klonen mit ssh verwenden werden.

<img src="screens/new-repo-2.png" width="00">


## Lokales Klonen des Repositorys, Konfiguration von Git, Erstellen der initialen Commits

Gehe in deinem Terminal zu dem Verzeichnis, in dem du dein lokales Git-Repository erstellen möchtest.

Klone das GitHub-Repository "MeinProjekt" mit dem folgenden Befehl: bash git clone git@github.com:DeinBenutzername/MeinProjekt.git .
Ersetze "DeinBenutzername" durch deinen GitHub-Benutzernamen. Der Befehl klont das Repository auf deinen lokalen Rechner.

Navigiere in das geklonte Verzeichnis "MeinProjekt":

    cd MeinProjekt

Konfiguriere `git` mit deinem Namen und E-Mail, die mit GitHub verknüpft sind:

    git config user.name "Dein Name"
    git config user.email "deine_email@beispiel.com"

<img src="screens/git-clone-project.png" width="600">


## Erstellen des "feature"-Branches

Hinzufügen einer neuen Datei zu diesem Branch und Committen der Änderungen.

<img src="screens/feature-branch-1.png" width="600">

Die Datei `main.py` wird geändert und comitted:

<img src="screens/feature-branch-2.png"  width="600">


## Mergen des "feature"-Branches in den "main"-Branch

Wechsel zum `main` branch. 
Nach dem Wechsel zuerst die `main.py` Datei ändern und dann commiten.

<img src="screens/feature-branch-3.png"  width="600">

Den Merge durchführen

<img src="screens/merge-0.png" width="500">

Öffne die Datei `main.py` und löse den Konflikt

<img src="screens/merge-1.png" width="500">

Aufgelöster Konflikt

<img src="screens/merge-1.5.png" width="600">
<img src="screens/merge-2.png" width="600">
<img src="screens/merge-3.png" width="600">

## Übertragen der Änderungen in das Remote repository

    git push