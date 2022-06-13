# Contributing to lists

Thank you for your interest in this project! Before making a contribution, please take a minute to read these guidelines.

If you have any questions about the project or these guidelines, [open an issue](https://github.com/jnv/lists/issues).

Most importantly, **have fun!** Don’t take this project _too_ seriously. While it is (hopefully) useful, there are better things in life than some arbitrary hoard of links.

## What Is Accepted

If you wish to add some project to this list, make sure it meets the following criteria:

* The project’s primary purpose is to be a list; it can be a list of recipes, favorite places in some city, learning resources…  The subject doesn’t matter.
* The project should contain the list of resources in some form; i.e., if the resources are stored in some database and the project contains only a backend code, it won’t be accepted.
* The project should be open to contributions; it doesn’t have to be hosted on GitHub, but anyone should be able to send a pull request or its equivalent.
* The project can be forked, cloned and maintained without reliance on the original source.
* Non-English lists and lists about non-technical subjects are very welcome!

## Adding a List

Lists are alphabetically sorted, so find a proper place to put your list in and an item in the following format:

```md
* [repository-name](https://github.com/author/repository-name) – Optional short description.
```

In your commit message, write:

```
Add repository-name
```

Keep one list to one commit and make separate pull requests for every list.

In your pull request, please put the list’s URL into the description, it is easier to review it.

Link’s description (`repository-name` in the example above) should be the original repository name. For example, given the repository `author/my-awesome-list-of-pancakes`, use `my-awesome-list-of-pancakes` for link’s description, not `My Awesome List of Pancakes` or even `Pancakes`.

Add a short description if the repository name is not obvious enough or to improve searchability. For example, `awesome-php` is most likely about PHP, while `cscs` is not obvious, so it is explained in the description (_Coding Style Conventions and Standards._).

Avoid using _List of…_ or _A curated list of…_ and similar in the description. It is redundant.

You can use the description for linking or describing a less known subject of the list. For example, `awesome-sarl` is about a rather less known SARL programming language, so the description states: _Resources for [SARL](http://www.sarl.io/) Agent-Oriented Programming Language._

If the list is not in English, state its language. The list’s description can also be in the list’s language. For example:

* [awesome-awesomeness-zh_CN](https://github.com/justjavac/awesome-awesomeness-zh_CN) _In Chinese_ – 中文版awesome list 系列文章`

If there are multiple lists with the same name by different authors, add the author’s username after the link, e.g., `recipes by @csswizardy`.

If there is a website for the list, add a link into the sub-item. For example, `awesome-ruby` has an official presentation at [awesome-ruby.com](http://awesome-ruby.com/), so in the list there is:

* [awesome-ruby](https://github.com/markets/awesome-ruby) by @markets
  - http://awesome-ruby.com/

### Technical and Non-technical Lists

Is your list related to software, programming, video games, or development activities? Then it is probably Technical. If the project’s name starts with `awesome`, put it into the [awesome-*](https://github.com/jnv/lists#awesome-) section.

If your list is related to cooking, fiction books, pictures, people or pretty much anything a non-programmer can relate to, then your project is likely Non-Technical and should be sorted as such.

When in doubt, [just ask](https://github.com/jnv/lists/issues). Or just send a pull request, we’ll sort it out.

## Removing Lists

You are welcome to propose a removal or change of an existing entry if:

* The project is not available anymore (e.g., the repository was deleted, or the user account was closed),
* the project has been moved to a new URL (e.g., project was moved under an organization).

Lack of activity in the project or duplication with other projects are not reasons for removal.
