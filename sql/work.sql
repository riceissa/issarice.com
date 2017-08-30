drop table if exists individual_tasks;

create table individual_tasks(
    task_id int(11) not null auto_increment primary key,
    task_venue enum('Wikipedia','Wikipedia Views','Effective Altruism Forum','LessWrong','Personal website','Wikimedia meta','wikiHow','Quora','Market subwiki','Donations list website', 'Contract work for Vipul Naik','Timelines wiki','None','Wikiquote','Vim Tips Wiki','Effective Altruism Wiki','Cognito Mentoring Information Wiki','Cause Prioritization Wiki','GitHub') default 'Wikipedia',
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
;

insert into individual_tasks(task_venue, task_type, task_receptacle, task_receptacle_url, completion_date, payment, topic, format, notes, language) values
    ('Wikipedia', 'Wikipedia page translation', '効果的利他主義', 'https://ja.wikipedia.org/wiki/%E5%8A%B9%E6%9E%9C%E7%9A%84%E5%88%A9%E4%BB%96%E4%B8%BB%E7%BE%A9', '2014-10-13', 0, 'Philanthropy', 'Prose', 'A partial translation of the English effective altruism page https://en.wikipedia.org/wiki/Effective_altruism', 'ja')
;
