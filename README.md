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

  <h1 align="center">🧞‍♂️ CacheGenius</h3>

  <p align="center">
    Speed-up your code by automatically identifying functions that should use caching!
    <br />
<!--
    <a href="https://github.com/NicolasMICAUX/cachegenius"><strong>Explore the docs »</strong></a>
-->
    <br />
    <br />
    <a href="https://github.com/NicolasMICAUX/cachegenius">View Demo</a>
    ·
    <a href="https://github.com/NicolasMICAUX/cachegenius/issues">Report Bug</a>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [Screen Shot][product-screenshot] -->
Have you ever spent hours trying to speed up some code, only to finally realize you're computing the same things 2 or 3 times, which means some caching does the trick ? What a waste of time !

🧞‍♂️ CacheGenius automatically identifies functions that should use caching in your code, so you can speed-up your code effortlessly!

<!-- GETTING STARTED -->
## Getting Started
Using CacheGenius is very simple.

Install CacheGenius with pip :
```sh
pip install cachegenius
```

To analyse an entire module `mypackage`, with all the functions and methods it contains, add this lines at the begginning of your code:
```python
import mypackage
import cachegenius

cachegenius(mypackage)
```

Now, use your module functions as usual. CacheGenius will automatically analyze all the functions you call, and will tell you if you should use caching or not.
```
>>> cachegenius.report()
Function: mokemodule.mokescript.my_func
Should cache: True
```

## Advanced usage
You can use the different parameters of `cachegenius.report()` to change the temporary files path, and print more infos using `debug`.  
Two parameters are available to tune the cost of computing and memory, that are used to decide if caching is worth it or not.

```python
def report(
    autocache_path: str       = "cachegenius_data/",
    debug: bool               = True,
    cost_per_comput_hr: float = 0.1,  # $/hr
    cost_per_mem_gb: float    = 0.2   # $/gb
)
```
You can clean all temporary files with `cachegenius.empty()`.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



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


## Authors
This library was created by [Nicolas MICAUX](https://github.com/NicolasMICAUX).


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
[//]: # ([linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)
[//]: # ([linkedin-url]: https://linkedin.com/in/othneildrew)
[product-screenshot]: images/screenshot.png

