[![Board Status](https://dev.azure.com/SGVisit/e635ec35-560a-4edc-bc08-7f3d68a05b54/2099dcf2-d96a-4699-8a6e-1155aad93b16/_apis/work/boardbadge/55a59400-5e3d-457c-a401-d2cd0178500f?columnOptions=1)](https://dev.azure.com/SGVisit/e635ec35-560a-4edc-bc08-7f3d68a05b54/_boards/board/t/2099dcf2-d96a-4699-8a6e-1155aad93b16/Microsoft.RequirementCategory)
# CityU CS Singapore Visit

Hello, this is the repository for the CityU CS Singapore Visit website. The preview is available at the repository's [Github Page](https://h11maitree.github.io/SGVisit/)

## Prerequisites

- **Ruby 3.0.0**,  [Ruby install/update instruction](https://stackoverflow.com/a/38194139)`
- **Jekyll**
`$ gem install jekyll`
- **Jekyll Bundler**,  Installation: 
`$ gem install jekyll bundler` 
`$ bundle install` //Install all project package

## Initiate the Service
Jekyll, a Ruby framework, is utilized to generate **static websites**. Throughout the web development process, all of the content and components (like Templates and MarkDowns) need to be compiled or baked into the final static files, such as HTML, CSS, and JS files. As such, it is crucial to initiate the 'watch' function during site modifications. This allows real-time tracking of any changes made, which can then be readily seen on your local development environment.

    $ bundle exec jekyll serve

## Add Pages
You can add pages into the site by creating a new MarkDown or HTML file in the folder **_posts** each file represent each post see [example post](./_posts/2023-06-05-day-one.markdown)

**Naming the file**
pleases be reminded that the file name need to follow the convention **"YYYY-MM-DD-POST-NAME-WITH-NO-SPACE" otherwise the framework will not recognize the post and will not be display**

**File type**
The post can be written both by 
- YYYY-MM-DD-POST-NAME-WITH-NO-SPACE.html
- YYYY-MM-DD-POST-NAME-WITH-NO-SPACE..markdown

**File Header**
Each page should have a header 

    ---
    layout: post
    title: "AI Class at NUS"
    date: 2023-06-02 10:42:55 +0800
    categories: students-exploration
    ---
    {Follow by HTML or MarkDown code}

**Post Categories**
We've recently updated the Home page to showcase each category separately. As such, it's vital that **every post has a valid category assigned; without one, the post will not be visible on the Home page**.

Here are the accepted categories:

- **academic-visit**: This category is designated for posts related to academic visits. This includes Lab visits, Lectures, and Office visits.
- **group-meal**: Use this for posts about official group meals hosted by professors.
- **students-exploration**: This category is intended for posts related to student self-exploration.
- **a**: If you haven't decided on a category yet, use this placeholder.

Please ensure to select an appropriate category when posting.

**Useful Link**
 - [Include features, import a component html into markdown/another html](https://jekyllrb.com/docs/includes/)
 - [MarkDown Editor](https://stackedit.io/app#)

## Inter-Page Linking
Since this website is intended to be a subpage of a larger website, it is important to include the site's base URL in all inter-page and resource links. This ensures that the links function correctly and direct users to the desired pages.
Below is an example of a **correct inter-page link**, where the base URL is properly included:

	<a  href="{{ site.baseurl }}/team"> The Team </a>
On the other hand, here is an example of an **incorrect inter-page link** that does not include the base URL:

	<a  href="/team"> The Team </a>
By omitting the base URL in the link, it may lead to broken or misdirected links, resulting in a poor user experience. Therefore, it is crucial to adhere to the correct format for inter-page links by including the site's base URL.

## GitHub Page (GitHub.io)
It will automatically as you push, the baked html will reflex the repository GitHub.io page automatically. If it not update within 10 mins please check [Actions](https://github.com/H11Maitree/SGVisit/actions).