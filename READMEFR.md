# 🔴 DOOMLAUNCH

```
 ▄▖▄▖▖ ▖▖ ▄▖▖▖▖ ▖▄▖▖▖
 ▌▌▌▌▌▌▛▖▞▌▌ ▌▌▌▌▛▖▌▌
 ▙▌ ▙▘▙▌▙▌▌▝ ▌▙▖▛▌▙▌▌▝▌▙▖▌▌
```

> **Lanceur Doom par Glisser-Déposer pour terminal Linux** — Lancez n'importe quel fichier `.pk3` ou `.wad` en un geste.

---

## ✨ Fonctionnalités

- 🎨 **Bannière ASCII animée arc-en-ciel** au démarrage
- 🖱️ **Vrai glisser-déposer** — faites glisser votre fichier dans le terminal et appuyez sur Entrée
- 🔍 **Détection automatique** de GZDoom, ZDoom, LZDoom, Crispy-Doom et PrBoom
- 🎮 **Sélecteur d'IWAD** — choisissez Doom 1 ou Doom 2, localisé automatiquement dans les dossiers courants
- 📁 Compatible `.pk3`, `.wad`, `.pk7`, `.ipk3`
- ✅ Confirmation avec aperçu de la commande complète avant le lancement
- ⌨️ Fonctionne en argument de commande ou en mode interactif complet

---

## 📋 Prérequis

- **Python 3.6+** (préinstallé sur la plupart des distributions Linux)
- Un **moteur Doom** : [GZDoom](https://zdoom.org/downloads), ZDoom, LZDoom, Crispy-Doom ou PrBoom
- Un fichier **IWAD** : `doom.wad` (Doom 1) et/ou `doom2.wad` (Doom 2)

---

## 🚀 Installation

### Option 1 — Rapide (lancer depuis un dossier)

```bash
git clone https://github.com/yourname/doomlaunch.git
cd doomlaunch
chmod +x doomlaunch.py
./doomlaunch.py
```

### Option 2 — Installation globale (utiliser depuis n'importe où)

```bash
sudo cp doomlaunch.py /usr/local/bin/doomlaunch
sudo chmod +x /usr/local/bin/doomlaunch
```

Vous pouvez maintenant taper `doomlaunch` depuis n'importe quel terminal.

---

## 🗂️ Configuration des IWAD

Placez vos fichiers WAD officiels de Doom dans l'un de ces dossiers (détectés automatiquement) :

| Chemin | Notes |
|--------|-------|
| `~/.local/share/doom/` | ✅ Recommandé |
| `~/doom/` | Dossier simple dans le home |
| `/usr/share/games/doom/` | Installation système |
| Dossier courant | Repli de secours |

Noms de fichiers IWAD supportés : `doom.wad`, `DOOM.WAD`, `doom1.wad`, `doom2.wad`, `DOOM2.WAD`

---

## 🎮 Utilisation

### Méthode 1 — Glisser-Déposer (le but principal !)

```bash
doomlaunch
```

Ensuite, **faites glisser votre fichier `.pk3` ou `.wad`** depuis votre gestionnaire de fichiers dans la fenêtre du terminal, puis appuyez sur **Entrée**.

### Méthode 2 — Argument direct

```bash
doomlaunch /chemin/vers/monmod.pk3
doomlaunch ~/Téléchargements/brutal_doom.wad
```

### Ce qui se passe ensuite ?

1. La bannière animée se lance 🎨
2. Vous choisissez **Doom 1** ou **Doom 2** comme jeu de base
3. Un résumé de la commande s'affiche
4. Confirmation → DOOM se lance 🔥

---

## 📖 Tutoriel pas à pas

### Étape 1 — Installer un moteur Doom

Sur Ubuntu/Debian :

```bash
sudo apt install gzdoom
```

Sur Fedora :

```bash
sudo dnf install gzdoom
```

Ou téléchargez manuellement depuis [zdoom.org/downloads](https://zdoom.org/downloads).

Vérifiez que l'installation fonctionne :

```bash
which gzdoom
# /usr/bin/gzdoom  ← vous devriez voir un chemin
```

---

### Étape 2 — Obtenir vos fichiers IWAD

Vous avez besoin des fichiers WAD **originaux et légaux** de Doom.  
Vous pouvez les acheter sur [Steam](https://store.steampowered.com/app/2280/) ou [GOG](https://www.gog.com/game/the_ultimate_doom).

Une fois obtenus, copiez-les dans le bon dossier :

```bash
mkdir -p ~/.local/share/doom
cp /chemin/vers/doom.wad ~/.local/share/doom/
cp /chemin/vers/doom2.wad ~/.local/share/doom/
```

Vérifiez qu'ils sont bien là :

```bash
ls ~/.local/share/doom/
# doom.wad  doom2.wad
```

---

### Étape 3 — Installer doomlaunch

```bash
# Cloner le dépôt
git clone https://github.com/yourname/doomlaunch.git
cd doomlaunch

# Rendre le script exécutable
chmod +x doomlaunch.py

# (Optionnel) Installer globalement
sudo cp doomlaunch.py /usr/local/bin/doomlaunch
sudo chmod +x /usr/local/bin/doomlaunch
```

---

### Étape 4 — Lancer un mod par glisser-déposer

1. Ouvrez votre **gestionnaire de fichiers** (Nautilus, Dolphin, Thunar, etc.)
2. Naviguez jusqu'à votre fichier `.pk3` ou `.wad`
3. Ouvrez un terminal et tapez :

```bash
doomlaunch
```

4. **Glissez le fichier** depuis le gestionnaire de fichiers **vers la fenêtre du terminal**
5. Le chemin apparaît automatiquement — appuyez sur **Entrée**
6. Choisissez **Doom 1** ou **Doom 2** :

```
  Choisissez votre IWAD:

  [1] DOOM 1  (/home/user/.local/share/doom/doom.wad)
  [2] DOOM 2  (/home/user/.local/share/doom/doom2.wad)
  [3] Chemin personnalisé

  Votre choix [1/2/3] → _
```

7. Un résumé s'affiche :

```
  ──────────────────────────────────────────────────
  ENGINE : gzdoom
  IWAD   : doom2.wad
  PWAD   : brutal_doom.pk3
  ──────────────────────────────────────────────────

  Lancer Doom ? [O/n] → _
```

8. Tapez **O** (ou appuyez sur Entrée) → 🔥 **DOOM SE LANCE !**

---

### Étape 5 — Astuce : alias pour encore plus de rapidité

Ajoutez ceci à votre `~/.bashrc` ou `~/.zshrc` :

```bash
alias dl='doomlaunch'
```

Rechargez le shell :

```bash
source ~/.bashrc
```

Maintenant vous pouvez juste taper `dl` et glisser votre fichier !

---

## 🔍 Ordre de détection des moteurs

doomlaunch cherche ces moteurs dans votre `PATH` dans cet ordre :

1. `gzdoom` ← préféré
2. `zdoom`
3. `lzdoom`
4. `crispy-doom`
5. `prboom-plus`
6. `prboom`

---

## ❓ Dépannage

**"Aucun moteur Doom trouvé"**
→ Installez GZDoom : `sudo apt install gzdoom`

**"doom.wad introuvable"**
→ Placez votre WAD dans `~/.local/share/doom/` et vérifiez l'orthographe du nom de fichier.

**Le drag & drop ne fonctionne pas**
→ Certains émulateurs de terminal ajoutent des guillemets autour du chemin — doomlaunch les retire automatiquement. Sinon, tapez ou collez le chemin manuellement.

**Le jeu se lance mais plante**
→ Vérifiez que votre IWAD correspond au mod (certains mods nécessitent Doom 2).

---

## 📁 Structure du projet

```
doomlaunch/
├── doomlaunch.py     # Script principal
└── README.md         # Ce fichier
```

---

## 🤝 Contribuer

Les pull requests sont les bienvenues ! Idées d'amélioration :

- Support de plusieurs fichiers PWAD en même temps
- Fichier de configuration pour les chemins par défaut
- Intégration shell avec complétion automatique
- Packaging Flatpak / AppImage

---

## 📜 Licence

Licence MIT — faites-en ce que vous voulez.

---

## 🩸 Fait avec

- Python 3
- Codes d'échappement ANSI
- Amour du terminal
- Et la motivation éternelle de **TOUT DÉCHIRER**
