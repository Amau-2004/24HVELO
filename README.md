# 24HVELO
Programme de suivi pour les 24h vélo.

Ce projet vise à créer un programme permettant de suivre et enregistrer les chronos des tours pendant les 24 heures vélo.
Le système permettra de suivre les performances du Vélo 1, du Vélo 2, ainsi que du peloton en temps réel.

## Utilisation

Deux scripts Python sont fournis :

- `24h_velo.py` : outil en ligne de commande pour enregistrer les tours et afficher un résumé.
- `sauvgarde.py` : module interne gérant la lecture et l'écriture du fichier de données JSON.

Pour ajouter un tour :
```bash
python 24h_velo.py add "Velo 1" 78.5
```

Pour afficher le résumé :
```bash
python 24h_velo.py summary
```

