//GLOBALS
var userchoice
var anychoice 
var savechoice 
var jsFeedUrl = "...";
var jsFeedTitle = null;

// Downloaded from https://feedburner.google.com/fb/feed-styles/bf30.js

// A workaround for XSL-to-XHTML systems that don't
//  implement XSL 'disable-output-escaping="yes"'.
//
// sburke@cpan.org, Sean M. Burke.
//  - I hereby release this JavaScript code into the public domain.

var is_decoding;
var DEBUG = 0;

function complaining (s) { alert(s);  return s; }

if(!(document.getElementById)) {

alert("Your browser cannot view this feed using FeedBurner's BrowserFriendly feature.\n\nConsider upgrading to Internet Explorer 6, Firefox, or Mozilla to view this feed and options for subscribing to its content in a news reader.");
	
}

function check_decoding () {
  var d = document.getElementById('cometestme');
  if(!d) {
    throw complaining("Can't find an id='cometestme' element?");
  } else if(!('textContent' in d)) {
    // It's a browser with a halfassed DOM implementation (like IE6)
    // that doesn't implement textContent!  Assume that if it's that
    // dumb, it probably doesn't implement disable-content-encoding.

  } else {
    ampy = d.textContent;
    if(DEBUG > 1) { alert("Got " + ampy); }

    if(ampy == undefined) throw complaining("'cometestme' element has undefined text content?!");
    if(ampy == ''       ) throw complaining("'cometestme' element has empty text content?!"    );

    if      (ampy == "\x26"	) { is_decoding =  true; }
    else if (ampy == "\x26amp;" ) { is_decoding = false; }
    else		     { throw complaining('Insane value: "' + ampy + '"!'); }
  }

  var msg =
   (is_decoding == undefined) ? "I can't tell whether the XSL processor supports disable-content-encoding!D"
   : is_decoding ? "The XSL processor DOES support disable-content-encoding"
   : "The XSL processor does NOT support disable-content-encoding"
  ;
  if(DEBUG) alert(msg);
  return msg;
}


function go_decoding () {

//	displayMajorSub();
	
  check_decoding();

  if(is_decoding) {
    DEBUG && alert("No work needs doing -- already decoded!");
    return;
  }

  var to_decode = document.getElementsByName('decodeable');
  if(!( to_decode && to_decode.length )) {
    DEBUG && alert("No work needs doing -- no elements to decode!");
    return;
  }


  var s;
  for(var i = to_decode.length - 1; i >= 0; i--) { 
    s = to_decode[i].textContent;

    if(
      s == undefined ||
      (s.indexOf('&') == -1 && s.indexOf('<') == -1)
    ) {
      // the null or markupless element needs no reworking
    } else {
      to_decode[i].innerHTML = s;  // that's the magic
    }
  }

  return;
}


//End


function displayMajorSub() {
	//October 2005 addition to show/hide PC/MAC buttons for subscription to ITMS/YME
	var macBtn = document.getElementById("subscribeITMS");
	var pcBtn = document.getElementById("subscribeYME");		


		if(navigator.platform.indexOf('Mac') > -1) { 
			pcBtn.style.display='none';
			macBtn.style.display='';
	} else {
			pcBtn.style.display=''
		}
	return;
}

//utility function for appending USM or pcast param on existing URL, parameterized or otherwise
function encodeParam(theURL, theFormat) {

	var rslt = "XXX";

	if (theURL.indexOf('?') > 0) {
		rslt = encodeURI(theURL + "&format=" + theFormat);
	} else {
		rslt = theURL + "?format=" + theFormat;
	}

	return rslt;

}

function subscribeNowUltra(readerHref,readerString) {
	eFURL = readerHref;

	//retrieve saveChoice value
	var saved = document.getElementById("savechoice");
	
	//strip current URL; replace with {feed} for posterity
	var reURL = /(.+)http.+$/

	//handle the itpc protocol case as well
	var reITPC = /(itpc:\/\/).+$/;

	if (reURL.test(readerHref)) {
		eFURL = eFURL.replace(reURL,'$1{feed}')
	} else if (reITPC.test(readerHref)) {
		eFURL = eFURL.replace(reITPC,'$1{feed}')
	}


	//if checked, write that subscribe URL as a cookie
	if (saved.value == "standard") {
		//store cookieReaderHref, replacing any existing value		
		//store reader string, too
		createCookie("fb_cookieReaderHref",eFURL,1000);
		createCookie("fb_readerString",readerString,1000);
	} else if (saved.value == "podcast") {
		//stored for podcast
		createCookie("fb_podcast_cookieReaderHref",eFURL,1000);
		createCookie("fb_podcast_readerString",readerString,1000);
	}
	
	//send location.href off to that loc'n	
	return readerHref;


}


function subscribeNow(readerHref,readerString) {
	
	//encode feedURL as needed; pre-decode is for friggin' Pluck title
	eFURL = decodeURI(readerHref);
	eFURL = encodeURI(eFURL);
	var cookieReaderHref = "";

	//save web, USM, feed://, pcast variants
	switch (readerString) {
		
		case "--":
			break
			//this is for IE, which doesn't respect disabled=disabled on the <option>
		
		case "USM": //Manage Services
			localref = document.location.href + "?format=usm"
			cookieReaderHref = localref
			eFURL = localref
			break;

		case "Plusmo":
			cookieReaderHref = "http://plusmo.com/add?url={feed}"
			break;

		case "Windows Live":
			cookieReaderHref = "http://www.live.com/?addFeed={feed}"
			break;

		case "Google":
			cookieReaderHref = "http://fusion.google.com/add?feedurl={feed}"
			break;
		
		case "My Yahoo!":
			cookieReaderHref = "http://add.my.yahoo.com/rss?url={feed}"
			break;

		case "Feedly":
			cookieReaderHref = "http://feedly.com/#subscription/feed/{feed}"
			break;

		case "SubToMe":
			cookieReaderHref = "https://www.subtome.com/#/subscribe?feeds={feed}"
			break;

		case "NewsGator Online":
			cookieReaderHref = "http://www.newsgator.com/ngs/subscriber/subext.aspx?url={feed}"
			break;
						
		case "My AOL":
			cookieReaderHref = "http://feeds.my.aol.com/add.jsp?url={feed}"
			break;
			
		case "Rojo":
			cookieReaderHref = "http://www.rojo.com/add-subscription?resource={feed}"
			break;
		
		case "Bloglines":
			cookieReaderHref = "http://www.bloglines.com/sub/{feed}"
			break;
						
		case "podnova":
			cookieReaderHref = "http://www.podnova.com/add.srf?url={feed}"
			break;

		case "Netvibes":
			cookieReaderHref = "http://www.netvibes.com/subscribe.php?url={feed}"
			break;

		case "Livedoor":
			cookieReaderHref = "http://reader.livedoor.com/subscribe/{feed}";
			break;

		case "My Yahoo! Japan": //japan
			cookieReaderHref = "http://add.my.yahoo.co.jp/rss?url={feed}"
			break;

		case "feedpath": 
			cookieReaderHref = "http://feedpath.jp/feedreader/feeds_add?url={feed}"
			break;

    case "sleipnir":
      cookieReaderHref = "http://www.fenrir.co.jp/rd/?rss={feed}"
      break;

    case "ExciteJP":
      cookieReaderHref = "http://reader.excite.co.jp/subscribe/?url={feed}"
      break;

    case "yandex":
      cookieReaderHref = "https://mail.yandex.ru/my/#lenta/feed/{feed}"
      break;

    case "iTunes": //mac pcast
			cookieReaderHref = "pcast://{feed}"
			noProtocolFeedUrl = jsFeedUrl.substr(7)
			eFURL = "pcast://" + encodeURI(noProtocolFeedUrl);
			break;

		case "iTunes/Yahoo Music Engine": //pc pcast
			cookieReaderHref = document.location.href + "?format=pcast"
			eFURL = document.location.href + "?format=pcast"
			break;

        default:
			cookieReaderHref = "feed:{feed}"
			eFURL = "feed:" + eFURL;
			readerString = "Subscribe with " + readerString;
	}

	//retrieve saveChoice value
	var saved = document.getElementById("savechoice");

	//if checked, write that subscribe URL as a cookie
	if (saved.value == "standard") {
		//store cookieReaderHref, replacing any existing value		
		//store reader string, too
		createCookie("fb_cookieReaderHref",cookieReaderHref,1000);
		createCookie("fb_readerString",readerString,1000);
	} else if (saved.value == "podcast") {
		//stored for podcast
		createCookie("fb_podcast_cookieReaderHref",cookieReaderHref,1000);
		createCookie("fb_podcast_readerString",readerString,1000);
	}
	
	//send location.href off to that loc'n	
	return eFURL;
}

function loadSubscribeAreaUltra(theme) {

	userchoice = document.getElementById("subscribe-userchoice");
	anychoice = document.getElementById("subscribe-options");
	//savechoice =  document.getElementById("savemychoice");
	var rHref ="";	
	var readerHref = null;
	var readerString = null;
	
	//cookied? display shorthand; else standard
	if (theme == "standard") {
		readerHref = readCookie("fb_cookieReaderHref");
		readerString = readCookie("fb_readerString");
	} else if (theme == "podcast") {
		readerHref = readCookie("fb_podcast_cookieReaderHref");
		readerString = readCookie("fb_podcast_readerString");	
	}
	
	if ((readerHref && readerString)) {

		var theLink = document.getElementById("subscribeLink").getElementsByTagName("a");

		var reFeed = /{feed}/
		
		//strip http:// from jsFeedUrl if ITPC or other protocol-bearing format
		if (readerHref.indexOf("itpc://")!=-1) {
			jsFeedUrl = jsFeedUrl.substring(7);
		}

		//remember jsFeedUrl is set at body onload
		rHref = readerHref.replace(reFeed,jsFeedUrl);

		//legacy cookie support
		reSubsText = /Subscribe with /;
		if (!reSubsText.test(readerString)) readerString = "Subscribe with " + readerString;

		theLink[0].href = rHref;
		theLink[0].innerHTML = readerString;
	
		//shorthand

		userchoice.style.display="";
		anychoice.style.display = "none";
	}
	
}

function loadSubscribeArea(theme) {

	userchoice = document.getElementById("subscribe-userchoice");
	anychoice = document.getElementById("subscribe-options");
	//savechoice =  document.getElementById("savemychoice");
	var noProtocolFeedUrl = "";
	var rHref ="";	
	var readerHref = null;
	var readerString = null;
	
	//cookied? display shorthand; else standard
	if (theme == "standard") {
		readerHref = readCookie("fb_cookieReaderHref");
		readerString = readCookie("fb_readerString");
	} else if (theme == "podcast") {
		readerHref = readCookie("fb_podcast_cookieReaderHref");
		readerString = readCookie("fb_podcast_readerString");	
	}
	
	if ((readerHref && readerString)) {

		var theLink = document.getElementById("subscribeLink").getElementsByTagName("a");

		//replace {feed} and optionally, {title}
		var reFeed = /{feed}/
		var reTitle = /{title}/
			
		//pcast protocol workaround
		if (readerHref.indexOf('pcast://')==0) {
			//remove pcast protocol from readerHref
			noProtocolFeedUrl = jsFeedUrl.substr(7)
			rHref = readerHref.replace(reFeed,noProtocolFeedUrl);
		} else {
			rHref = readerHref.replace(reFeed,jsFeedUrl);
		}

		if (jsFeedTitle) rHref = rHref.replace(reTitle,jsFeedTitle);

		theLink[0].href = rHref;
		theLink[0].innerHTML = "Subscribe with " + readerString;
	
		//shorthand

		userchoice.style.display="";
		anychoice.style.display = "none";
		//savechoice.style.display = "none";
	}
	
}

function clearUserchoice(theme) {
	if (theme == "standard") {
			eraseCookie("fb_cookieReaderHref");
			eraseCookie("fb_readerString");
	} else {
		eraseCookie("fb_podcast_cookieReaderHref");
		eraseCookie("fb_podcast_readerString");
		
	}
	
	userchoice.style.display="none";
	anychoice.style.display = "";
	//savechoice.style.display = "";
	
	return false;	
	
}

function createCookie(name,value,days)
{
	if (days)
	{
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name)
{
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++)
	{
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function eraseCookie(name)
{
	createCookie(name,"",-1);
}
