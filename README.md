

<h2 align="center">Welcome, Stranger!</h2>

<div align="center">
    <a href="https://github.com/optimizean">
        <img height=300 src="https://github.com/optimizean/optimizean/assets/172540472/4efc7d26-baac-4260-9e9b-a7cf1dfb292c"/>
    </a>
</div>

<div align="center">
 <a href="https://github.com/optimizean/profile-readme-package/actions/workflow/status/optimizean/profile-readme-package/python-package.yml?branch=main">
    <img src="https://img.shields.io/github/actions/workflow/status/optimizean/profile-readme-package/python-package.yml?branch=main&label=actions&style=flat-square" alt="workflow" style="height: 20px;">
  </a>
  <a href="https://github.com/optimizean/profile-readme-package/graphs/contributors">
    <img src="https://img.shields.io/github/contributors-anon/optimizean/profile-readme-package?color=yellow&style=flat-square" alt="contributors" style="height: 20px;">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/MIT-blue.svg?style=flat-square&label=license" alt="license" style="height: 20px;">
  </a>

</div>


<br/>
<br/>



## 🔬 What is this? 

Two lines are sufficient to express us! This Python package provides personal details just like the GitHub profile README. What you need is Python 3.8 and your own terminal. This package is build with 95% Python, only because I am born to be a python developer. `Minimized dependencies to 1~2` to keep clean environment, except rich which can colorize terminal. 


## ❓ Why is it needed? 

> Developers tell their story through their code.

I discovered that an enormous amount of time is spent browsing profile components and selecting them. Almost every developer uses GitHub, and GitHub is for all developers. Therefore, I believe that visitors who stop by others' GitHub profiles are likely `Code-Friendly` individuals. The service is meant to build store our own code, Even so, it's too much to browse through every repository of theirs. 

More importantly, some developers feel more at ease reading code rather than long description or fancy icons. So, why don't we express ourselves through our code snippet?  

<sub>*(v1.1.2: Just for now, this is only for me. I'll plan to extend it.)*</sub>



## 📂 How it works? 

Anyone who encounters this will follow the steps below

```bash
pip install optimizean
optimizean
pip uninstall optimizean    # after you use it.
```

![v111-1](https://github.com/optimizean/profile-readme-package/assets/172540472/802ec573-b7e7-4379-b76e-be216199e8e8)

### Authorizing Step
> Only for fancy, But realtime update. How many visitors do you have?<br/>

<img width="900" alt="v112" src="https://github.com/optimizean/profile-readme-package/assets/172540472/848c46e7-9ed1-447e-b322-9d312fba0f5c">

In this step, the user will be assigned a specific number which refers to installation counts. After the terminal screen is cleared, localized greetings will appear.


### Greeting Step

> Customized a simple greeting message for surprise. What message did you get?

<img width="900" alt="v112" src="https://github.com/optimizean/profile-readme-package/assets/172540472/91e4396f-a555-4b85-b8b6-d75b1dd86e09">

The module detects the user's operating system and local time to select the proper welcoming message. Currently, it supports 'AR', 'DE', 'ES', 'FR', 'HI', 'IT', 'JA', 'KR', 'PT', 'RU', 'US', and 'ZH'. <br/>
- Note: Local customized greetings only use Python's internal modules os and time. Your personal information is safe and not stored or leaked.
- I am trying hard not to harm your system or environment. If you find any of them, please report an [issue](https://github.com/optimizean/READO/issues/new/choose)

### Personal Info

> The main contents, an essence for this project.

<img width="900" alt="v112" src="https://github.com/optimizean/profile-readme-package/assets/172540472/070b51b3-79d6-4828-a164-3126f3be313e">
<sub>(v1.1.2) Temporal Note: If anyone wants to customize this, you can modify `src/optimizean/contents.py`</sub>

## 📬 Where to contact? 

If you want to contact me, do not hesitate to email or create an issue. You can also fork the repository and customize it too.

## ❗ License

[MIT License](https://github.com/optimizean/profile-readme-package/blob/main/LICENSE)