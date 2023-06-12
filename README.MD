[![Board Status](https://dev.azure.com/SGVisit/e635ec35-560a-4edc-bc08-7f3d68a05b54/2099dcf2-d96a-4699-8a6e-1155aad93b16/_apis/work/boardbadge/55a59400-5e3d-457c-a401-d2cd0178500f)](https://dev.azure.com/SGVisit/e635ec35-560a-4edc-bc08-7f3d68a05b54/_boards/board/t/2099dcf2-d96a-4699-8a6e-1155aad93b16/Microsoft.RequirementCategory)
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
    categories: Aducation
    ---
    {Follow by HTML or MarkDown code}
 **Useful Link**
 - [Include features, import a component html into markdown/another html](https://jekyllrb.com/docs/includes/)
 - [MarkDown Editor](https://stackedit.io/app#)

## GitHub Page (GitHub.io)
It will automatically as you push, the baked html will reflex the repository GitHub.io page automatically.