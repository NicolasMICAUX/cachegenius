<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]<!--[![Forks][forks-shield]][forks-url]-->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]<!--[![MIT License][license-shield]][license-url]--><!--[![LinkedIn][linkedin-shield]][linkedin-url]-->
[![PyPi version][pypi-shield]][pypi-url]<!--[![Python 2][python2-shield]][python-url]-->
[![Python 3][python3-shield]][python-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/NicolasMICAUX/cachegenius">
    <img src="https://raw.githubusercontent.com/NicolasMICAUX/cachegenius/main/images/logo.jpg" alt="Logo" width="160" height="160">
  </a>
  <h1 align="center">CacheGenius</h3>
  <p align="center">
Accélérez votre code en détectant automatiquement les fonctions qui devraient utiliser la mise en cache !<br/>
<!--
    <a href="https://github.com/NicolasMICAUX/cachegenius"><strong>Explorer la documentation »</strong></a>
-->
    <br/><br/>
    <a href="https://github.com/NicolasMICAUX/cachegenius">Voir la démo</a>
    ·
    <a href="https://github.com/NicolasMICAUX/cachegenius/issues">Report Bug</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Introduction
<!-- [Screen Shot][product-screenshot] -->
Avez-vous déjà passé des heures à rendre un code plus rapide, pour finalement réaliser que vous calculez les mêmes choses 2 ou 3 fois, ce qui fait qu'un peu de mise en cache ferait largement l'affaire ? Quelle perte de temps !

🧞‍♂️ CacheGenius identifie automatiquement les fonctions qui devraient utiliser la mise en cache dans votre code, afin que vous puissiez l'accélérer sans aucun effort !

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- GETTING STARTED -->
## Pour commencer
CacheGenius est très simple à utiliser.

Installer CacheGenius avec pip :
```sh
pip install cachegenius
```

Pour analyser un module entier `mypackage`, avec toutes les fonctions et méthodes qu'il contient, ajoutez ces lignes au début de votre code :
``python
import mypackage
import cachegenius

cachegenius(mypackage)
```

Maintenant, utilisez les fonctions de votre module comme d'habitude. CacheGenius analysera automatiquement toutes les fonctions que vous appelez, et vous dira si vous devez utiliser la mise en cache ou non.
```
>>> cachegenius.report()
Function: mokemodule.mokescript.my_func
Should cache: True
```

## Utilisation avancée
Vous pouvez utiliser les différents paramètres de `cachegenius.report()` : pour changer le chemin des fichiers temporaires, et afficher plus d'informations en utilisant `debug`.  
Deux paramètres sont disponibles pour ajuster le coût du calcul et de la mémoire, qui sont utilisés pour décider si la mise en cache vaut la peine ou non.

```python
def report(
    autocache_path: str       = "cachegenius_data/",
    debug: bool               = True,
    cost_per_comput_hr: float = 0.1,  # $/hr
    cost_per_mem_gb: float    = 0.2   # $/gb
)
```
Vous pouvez nettoyer tous les fichiers temporaires avec `cachegenius.empty()`.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>


<!-- CONTRIBUTING -->
<!--
## Contributing
_(Section in english)_  

### Roadmap/todo
| Task | Importance | Difficulty | Contributor on it | Description  |
|:-----|------------|------------|-------------------|:-------------|
|      | ./5        | ./5        | NOBODY            | _e.g._ : ... |

Non-Code contribution :

| Task | Importance | Difficulty | Contributor on it | Description  |
|:-----|------------|------------|-------------------|:-------------|
|      | ./5        | ./5        | NOBODY            | _e.g._ : ... |


_For every todo, just click on the link to find the discussion where I describe how I would do it._  
See the [open issues](https://github.com/NicolasMICAUX/cachegenius/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->

### How to contribute
Contributing is an awesome way to learn, inspire, and help others. Any contributions you make are **greatly appreciated**, even if it's just about styling and best practices.

If you have a suggestion that would make this project better, please fork the repo and create a pull request.  
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Auteurs
Cette librairie a été crée par [Nicolas MICAUX](https://github.com/NicolasMICAUX).



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NicolasMICAUX/cachegenius.svg?style=for-the-badge
[contributors-url]: https://github.com/NicolasMICAUX/cachegenius/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/NicolasMICAUX/cachegenius.svg?style=for-the-badge
[stars-url]: https://github.com/NicolasMICAUX/cachegenius/stargazers
[issues-shield]: https://img.shields.io/github/issues/NicolasMICAUX/cachegenius.svg?style=for-the-badge
[issues-url]: https://github.com/NicolasMICAUX/cachegenius/issues
[pypi-shield]: https://img.shields.io/pypi/v/cachegenius.svg?style=for-the-badge
[pypi-url]: https://pypi.org/project/cachegenius/
[python2-shield]: https://img.shields.io/badge/python-2.7+-blue.svg?style=for-the-badge
[python3-shield]: https://img.shields.io/badge/python-3.5+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/

[//]: # ([license-shield]: https://img.shields.io/github/license/NicolasMICAUX/cachegenius.svg?style=for-the-badge)
[//]: # ([license-url]: https://github.com/NicolasMICAUX/cachegenius/blob/master/LICENSE.txt)
[//]: # ([product-screenshot]: images/screenshot.png)

