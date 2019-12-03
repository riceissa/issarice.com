# License: CC0

# This file only includes tasks outside of my contract work for Vipul Naik and
# Peter Hurford. For tasks I did as part of contract work for them, see
# https://github.com/vipulnaik/contractwork/tree/master/sql

drop table if exists individual_tasks;

create table individual_tasks(
    task_id int(11) not null auto_increment primary key,
    task_venue enum('Wikipedia','Wikipedia Views','Effective Altruism Forum','LessWrong','LessWrong Wiki','Personal website','Wikimedia meta','wikiHow','Quora','Market subwiki','Donations list website', 'Contract work for Vipul Naik','Timelines wiki','None','Wikiquote','Vim Tips Wiki','Effective Altruism Wiki','Cognito Mentoring Information Wiki','Cause Prioritization Wiki','GitHub') default 'Wikipedia',
    task_type enum('Wikipedia page creation','Wikipedia page update','Wikipedia page translation','Attempted Wikipedia work','Miscellaneous Wikipedia work','Preliminary research','Blog post or article','Survey creation','Survey recruitment','Coding','Consulting','Review','Wiki page creation','Wiki page update','Questions and answers','Contacting people','Data entry','Task listing','Content migration','Timelines page creation','Timelines page update','Worker onboarding and assistance'),
    task_receptacle varchar(200) NOT NULL,
    task_receptacle_url varchar(200) NOT NULL,
    completion_date date NOT NULL,
    payment float(7,2) NOT NULL,
    topic varchar(100) NOT NULL,
    format varchar(100) NOT NULL,
    notes varchar(2000) DEFAULT NULL,
    private boolean DEFAULT false,
    language enum('en','ja') COLLATE utf8_unicode_ci DEFAULT 'en',
    payer enum('Vipul Naik', 'Peter Hurford') default NULL
) ENGINE=InnoDB AUTO_INCREMENT=15239276 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into individual_tasks(task_venue, task_type, task_receptacle, task_receptacle_url, completion_date, payment, topic, format, notes) values
    ('Personal website', 'Blog post or article', 'Open Philanthropy Project non-grant funding', 'https://issarice.com/open-philanthropy-project-non-grant-funding', '2017-04-02', 0, 'Philanthropy/Open Philanthropy Project', 'Prose', 'Decided on a whim to collect data')
    ,('Wikipedia', 'Wikipedia page creation', 'Timeline of online dating services', 'https://en.wikipedia.org/wiki/Timeline_of_online_dating_services', '2015-10-20', 0, 'Technology', 'Prose', 'Originally created on the Cause Prioritization Wiki as Timeline of technology-assisted dating services https://causeprioritization.org/Timeline%20of%20technology-assisted%20dating%20services but later moved to Wikipedia')
    ,('Wikipedia', 'Wikipedia page creation', 'Person-affecting view', 'https://en.wikipedia.org/wiki/Person-affecting_view', '2015-10-24', 0, 'Population ethics', 'Prose', NULL)
    ,('Wikipedia', 'Wikipedia page creation', 'fugitive.vim', 'https://en.wikipedia.org/wiki/Fugitive.vim', '2017-02-25', 0, 'Technology', 'Prose', NULL)
    ,('Wikipedia', 'Wikipedia page creation', 'ICWATCH', 'https://en.wikipedia.org/wiki/ICWATCH', '2017-02-26', 0, 'Technology', 'Prose', 'I discovered ICWATCH while adding events to Timeline of LinkedIn https://en.wikipedia.org/w/index.php?title=Timeline_of_LinkedIn&oldid=766908994#cite_ref-59 , specifically from a TechCrunch article https://techcrunch.com/2016/08/15/linkedin-sues-scrapers/')
    ,('Wikipedia', 'Wikipedia page creation', 'Unlicense', 'https://en.wikipedia.org/wiki/Unlicense', '2017-02-28', 0, 'Technology', 'Prose', 'I think I decided on a whim to create the page. Personally I prefer CC0 as a public domain license.')
    ,('Wikipedia', 'Wikipedia page creation', 'Nonidentity problem', 'https://en.wikipedia.org/wiki/Nonidentity_problem', '2015-12-18', 0, 'Population ethics', 'Prose', NULL)
    ,('Wikiquote', 'Wiki page creation', 'Michael Vassar', 'https://en.wikiquote.org/wiki/Michael_Vassar', '2017-07-14', 0, 'Rationality improvement', 'Prose', 'I kept hearing people talk about Michael Vassar, and was frustrated that there was no canonical place to look at quotes about him.')
    ,('Timelines wiki', 'Wiki page creation', 'Timeline of TempleOS', 'https://timelines.issarice.com/wiki/Timeline_of_TempleOS', '2017-03-24', 0, 'Technology', 'Timeline', 'I have been fascinated by Terry A. Davis since discovering him on /g/. I wrote the timeline after getting frustrated at being unable to keep his life story straight in my head.')
    ,('Timelines wiki', 'Wiki page creation', 'Timeline of Carl Shulman publications', 'https://timelines.issarice.com/wiki/Timeline_of_Carl_Shulman_publications', '2017-06-05', 0, 'Rationality improvement', 'Timeline', 'Vipul Naik gave me the idea and provided funding through a stipend but no specific task payment')
    ,('Vim Tips Wiki', 'Wiki page creation', 'Unused keys', 'http://vim.wikia.com/wiki/Unused_keys?useskin=monobook', '2017-05-29', 0, 'Technology', 'Table', 'I got frustrated at being unable to quickly tell whether a key was safe to map in Vim.')
    ,('Vim Tips Wiki', 'Wiki page creation', 'Working with long lines', 'http://vim.wikia.com/wiki/Working_with_long_lines?useskin=monobook', '2016-11-04', 0, 'Technology', 'Prose', NULL)
    ,('Vim Tips Wiki', 'Wiki page creation', 'Linting', 'http://vim.wikia.com/wiki/Linting?useskin=monobook', '2017-08-02', 0, 'Technology', 'Prose', NULL)
    ,('Effective Altruism Wiki', 'Wiki page update', 'Criticism of effective altruism', 'https://github.com/riceissa/issarice.com/blob/master/external/wiki.effectivealtruismhub.com/Criticism_of_effective_altruism.mediawiki', '2015-11-20', 0, 'Philanthropy', 'Prose', 'I did not create the page but began adding criticisms I encountered. Unfortunately the wiki seems to be gone.')
    ,('Cognito Mentoring Information Wiki', 'Wiki page creation', 'Using Reddit', 'https://info.cognitomentoring.org/wiki/Using_Reddit', '2015-07-30', 0, 'Technology', 'Prose', 'Vipul Naik provided me with an account on the wiki. I don’t remember the details of how the idea for creating the page came about. I don’t believe I was paid.')
    ,('Cause Prioritization Wiki', 'Coding', 'Cause Prioritization Wiki', 'https://causeprioritization.org/', '2014-11-28', 0, 'Philanthropy', 'Prose', 'Vipul Naik convinced me to create the website. The Git repository https://github.com/riceissa/causeprioritization has its initial commit on this day, and the domain was registered on this day https://whois.icann.org/en/lookup?name=causeprioritization.org')
    ,('GitHub', 'Coding', 'mediawiki.vim', 'https://github.com/riceissa/vim-mediawiki', '2017-08-13', 0, 'Technology', 'Code', 'As I began writing a lot of Wikipedia pages, I started to want a good filetype plugin. Not being able to find one I liked, I wrote my own. Development began on 2016-08-17 and I slowly added features as needed.')
    ,('GitHub', 'Coding', 'Citewebgen', 'https://github.com/riceissa/citewebgen', '2016-11-30', 0, 'Technology', 'Code', 'As I began writing a lot of Wikipedia pages, I wanted a quick way to cite web pages. Not being satisfied with existing scripts, I wrote my own.')
    ,('Personal website', 'Content migration', 'Deleted pages of gwern.net', 'https://files.issarice.com/gwern/', '2015-09-17', 0, 'Digital preservation', 'Prose', 'I wanted to conveniently see gwern’s deleted pages in compiled form.')
    ,('Timelines wiki', 'Wiki page creation', 'Domain names in timelines', 'https://timelines.issarice.com/wiki/Domain_names_in_timelines', '2017-08-25', 0, 'Content creation', 'Prose', NULL)
    ,('Timelines wiki', 'Wiki page creation', 'Representativeness of events in timelines', 'https://timelines.issarice.com/wiki/Representativeness_of_events_in_timelines', '2017-08-30', 0, 'Content creation', 'Prose', NULL)
    ,('Timelines wiki','Coding','Timelines Wiki main page table automation','https://github.com/riceissa/timelines-wiki-main-page-table','2017-10-16',0.00,'Miscellaneous','Code','Previously the main page table had been filled in manually by (mostly) me. This task allows for significantly faster data updates and more complete data.')
    ,('Personal website','Coding','change-theme.js','https://github.com/riceissa/issarice.com/blob/master/static/change-theme.js','2017-10-18',0.00,'User experience','Code','Some of my friends (i.e. the only semi-regular readers of my website as far as I know) have picky aesthetic tastes when it comes to website design, and so do I. After some recent design changes to my site I received a complaint, so this script is a compromise to allow readers to change limited aspects of the design. The code as of this initial round of development is at https://github.com/riceissa/issarice.com/blob/63854b5d5e798caa76ce20f1ae1ca52c9f736ef8/static/change-theme.js and some more information at https://issarice.com/text-width (though only about the text width part).')
    ,('LessWrong Wiki','Wiki page creation','Optimization daemons','https://wiki.lesswrong.com/wiki/Optimization_daemons','2018-02-08',0.0,'AI safety','Prose','A short page about optimization daemons, since there didn''t seem to be a single page that linked out to all other discussions.')
    ,('Timelines wiki','Timelines page creation','Timeline of Wei Dai publications','https://timelines.issarice.com/wiki/Timeline_of_Wei_Dai_publications','2018-02-16',0.0,'Rationality','Timeline','I''ve been getting interested in Wei Dai''s posts on LessWrong and other forums, so decided to make this timeline. Since the early everything-list posts were not easily accessible, I decided to host these through GitHub Pages. Vipul Naik allowed me to count this as work time for him, plus $35 per 8 hours of work on the timeline.')
    ,('Cause Prioritization Wiki','Wiki page creation','List of discussions between Paul Christiano and Wei Dai','https://causeprioritization.org/List_of_discussions_between_Paul_Christiano_and_Wei_Dai','2018-02-28',0.0,'AI safety','Table','As I''ve been reading more discussions of AI safety, I''ve been getting interested in the disagreements between Paul Christiano and Wei Dai, so I decided to make a list for easy reference. As of this writing, many of the "Topics covered" and "Summary" fields are not filled; I hope to fill these as I process the discussions. This page was created under general work on the Cause Prioritization Wiki (stipend plus $45 per 8 hours), for which pay will be entered separately.')
    ,('Wikiquote','Wiki page creation','Wei Dai','https://en.wikiquote.org/wiki/Wei_Dai','2018-04-05',0.00,'Rationality improvement','Prose','I spent a lot of time reading old LessWrong discussions in the course of writing some of my timelines and learning about decision theory, and realized there were enough good Wei Dai quotes for a page.')
    ,('Wikiquote','Wiki page creation','Holden Karnofsky','https://en.wikiquote.org/wiki/Holden_Karnofsky','2018-04-06',0.00,'Philanthropy','Prose','After writing the Wikiquote page for Wei Dai, I was in the mood to write another similar page, so I picked Holden Karnofsky (who I knew had some good quotes).')
    ,('Cause Prioritization Wiki','Wiki page creation','List of classifications of philanthropy','https://causeprioritization.org/List_of_classifications_of_philanthropy','2018-04-27',0.00,'Philanthropy','Table','In the process of thinking about how to better classify cause areas on the wiki, I discovered several existing classifications of philanthropy, so I decided to make a list with some notes on each.')
    ,('LessWrong Wiki','Wiki page creation','Escher painting mind','https://wiki.lesswrong.com/wiki/Escher_painting_mind','2018-10-04',0.00,'Rationality','Prose','I noticed this term being used in several of Eliezer Yudkowsky’s writings, and became frustrated that there was no location that collected all of these.')
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'Comparison of decision theories (with a focus on logical-counterfactual decision theories)', /* task_receptacle */
        'https://www.lesswrong.com/posts/QPhY8Nb7gtT5wvoPH/comparison-of-decision-theories-with-a-focus-on-logical', /* task_receptacle_url */
        '2019-03-16', /* completion_date */
        0.00, /* payment */
        'Decision theory', /* topic */
        'Prose', /* format */
        'A blog post comparing decision theories like UDT, FDT, and TDT, which are frequently discussed on LessWrong.' /* notes */
    )
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'Degree of duplication and coordination in projects that examine computing prices, AI progress, and related topics?', /* task_receptacle */
        'https://www.greaterwrong.com/posts/9YwNXt7ANyMqTu6Ky/degree-of-duplication-and-coordination-in-projects-that', /* task_receptacle_url */
        '2019-04-23', /* completion_date */
        0.00, /* payment */
        'AI safety', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'Inversion of theorems into definitions when generalizing', /* task_receptacle */
        'https://www.greaterwrong.com/posts/rs2focaRymwvkW2jS/inversion-of-theorems-into-definitions-when-generalizing', /* task_receptacle_url */
        '2019-08-04', /* completion_date */
        0.00, /* payment */
        'Mathematics', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'What are the differences between all the iterative/​recursive approaches to AI alignment?', /* task_receptacle */
        'https://www.greaterwrong.com/posts/cYduioQNeHALQAMre/what-are-the-differences-between-all-the-iterative-recursive', /* task_receptacle_url */
        '2019-09-20', /* completion_date */
        0.00, /* payment */
        'AI safety/iterated amplification', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'Deliberation as a method to find the “actual preferences” of humans', /* task_receptacle */
        'https://www.greaterwrong.com/posts/ebdf8GZxt3L9grwwN/deliberation-as-a-method-to-find-the-actual-preferences-of', /* task_receptacle_url */
        '2019-10-22', /* completion_date */
        0.00, /* payment */
        'AI safety', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'LessWrong', /* task_venue */
        'Blog post or article', /* task_type */
        'Is it harder to become a MIRI mathematician in 2019 compared to in 2013?', /* task_receptacle */
        'https://www.greaterwrong.com/posts/5syG88rmW5iD9kTM5/is-it-harder-to-become-a-miri-mathematician-in-2019-compared', /* task_receptacle_url */
        '2019-10-28', /* completion_date */
        0.00, /* payment */
        'AI safety', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'Effective Altruism Forum', /* task_venue */
        'Blog post or article', /* task_type */
        'Funding chains in the x-risk/AI safety ecosystem', /* task_receptacle */
        'https://eaforum.issarice.com/posts/hbSvxj7KuS7k4Ty6N/funding-chains-in-the-x-risk-ai-safety-ecosystem', /* task_receptacle_url */
        '2019-09-09', /* completion_date */
        0.00, /* payment */
        'AI safety', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
    ,(
        'LessWrong Wiki', /* task_venue */
        'Wiki page creation', /* task_type */
        'Do the math, then burn the math and go with your gut', /* task_receptacle */
        'https://wiki.lesswrong.com/wiki/Do_the_math%2C_then_burn_the_math_and_go_with_your_gut', /* task_receptacle_url */
        '2019-05-15', /* completion_date */
        0.00, /* payment */
        'Rationality', /* topic */
        'Prose', /* format */
        '' /* notes */
    )
;

insert into individual_tasks(task_venue, task_type, task_receptacle, task_receptacle_url, completion_date, payment, topic, format, notes, language) values
    ('Wikipedia', 'Wikipedia page translation', '効果的利他主義', 'https://ja.wikipedia.org/wiki/%E5%8A%B9%E6%9E%9C%E7%9A%84%E5%88%A9%E4%BB%96%E4%B8%BB%E7%BE%A9', '2014-10-13', 0, 'Philanthropy', 'Prose', 'A partial translation of the English effective altruism page https://en.wikipedia.org/wiki/Effective_altruism', 'ja')
;
