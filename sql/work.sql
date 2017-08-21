create table individual_tasks(
    task_id int(11) not null auto_increment primary key,
    task_venue enum('Wikipedia','Wikipedia Views','Effective Altruism Forum','LessWrong','Personal website','Wikimedia meta','wikiHow','Quora','Market subwiki','Donations list website', 'Contract work for Vipul Naik','Timelines wiki','None','issarice.com') default 'Wikipedia',
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
    payer enum('Vipul Naik', 'Peter Hurford') default 'Vipul Naik'
) ENGINE=InnoDB AUTO_INCREMENT=15239276 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into individual_tasks(task_venue, task_type, task_receptacle, task_receptacle_url, completion_date, payment, topic, format, notes) values
    ('issarice.com', 'Blog post or article', 'Open Philanthropy Project non-grant funding', 'https://issarice.com/open-philanthropy-project-non-grant-funding', '2017-04-02', 0, 'Philanthropy/Open Philanthropy Project', 'Prose', 'Decided on a whim to collect data')
;
