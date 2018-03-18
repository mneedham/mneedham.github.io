+++
draft = false
date="2015-11-24 00:12:59"
title="jq: Cannot iterate over number / string and number cannot be added"
tag=['jq']
category=['Software Development']
+++

<p>In my continued parsing of <a href="http://www.meetup.com/meetup_api/">meetup.com's JSON API</a> I wanted to extract some information from the following JSON file:</p>



~~~bash

$ head -n40 data/members/18313232.json
[
  {
    "status": "active",
    "city": "London",
    "name": ". .",
    "other_services": {},
    "country": "gb",
    "topics": [],
    "lon": -0.13,
    "joined": 1438866605000,
    "id": 92951932,
    "state": "17",
    "link": "http://www.meetup.com/members/92951932",
    "photo": {
      "thumb_link": "http://photos1.meetupstatic.com/photos/member/8/d/6/b/thumb_250896203.jpeg",
      "photo_id": 250896203,
      "highres_link": "http://photos1.meetupstatic.com/photos/member/8/d/6/b/highres_250896203.jpeg",
      "photo_link": "http://photos1.meetupstatic.com/photos/member/8/d/6/b/member_250896203.jpeg"
    },
    "lat": 51.49,
    "visited": 1446745707000,
    "self": {
      "common": {}
    }
  },
  {
    "status": "active",
    "city": "London",
    "name": "Abdelkader Idryssy",
    "other_services": {},
    "country": "gb",
    "topics": [
      {
        "name": "Weekend Adventures",
        "urlkey": "weekend-adventures",
        "id": 16438
      },
      {
        "name": "Community Building",
        "urlkey": "community-building",
~~~	

<p>
In particular I want to extract the member's id, name, join date and the ids of topics they're interested in. I started with the following jq query to try and extract those attributes:
</p>



~~~bash

$ jq -r '.[] | [.id, .name, .joined, (.topics[] | .id | join(";"))] | @csv' data/members/18313232.json
Cannot iterate over number (16438)
~~~

<p>
Annoyingly this treats topic ids on an individual basis rather than as an array as I wanted. I tweaked the query to the following with no luck:
</p>



~~~bash

$ jq -r '.[] | [.id, .name, .joined, (.topics[].id | join(";"))] | @csv' data/members/18313232.json
Cannot iterate over number (16438)
~~~

<p>
As a guess I decided to wrap '.topics[].id' in an array literal to see if it had any impact:
</p>



~~~bash

$ jq -r '.[] | [.id, .name, .joined, ([.topics[].id] | join(";"))] | @csv' data/members/18313232.json
92951932,". .",1438866605000,""
jq: error (at data/members/18313232.json:60013): string ("") and number (16438) cannot be added
~~~

<p>
Woot! A different error message at least and this one seems to be due to a type mismatch between the string we want to end up with and the array of numbers that we currently have. 
</p>


<p>We can cast our way to victory with the 'tostring' function:</p>



~~~r

$ jq -r '.[] | [.id, .name, .joined, ([.topics[].id | tostring] | join(";"))] | @csv' data/members/18313232.json
...
92951932,". .",1438866605000,""
193866304,"Abdelkader Idryssy",1445195325000,"16438;20727;15401;9760;20246;20923;3336;2767;242;58259;4417;1789;10454;20274;10232;563;25375;16433;15187;17635;26273;21808;933;7789;23884;16212;144477;15322;21067;3833;108403;20221;1201;182;15083;9696;4377;15360;18296;15121;17703;10161;1322;3880;18333;3485;15585;44584;18692;21681"
28643052,"Abhishek Chanda",1439688955000,"646052;520302;15167;563;65735;537492;646072;537502;24959;1025832;8599;31197;24410;26118;10579;1064;189;48471;16216;18062;33089;107633;46831;20479;1423042;86258;21441;3833;21681;188;9696;58162;20398;113032;18060;29971;55324;30928;15261;58259;638;16475;27591;10107;242;109595;10470;26384;72514;1461192"
39523062,"Adam Kinder-Jones",1438677474000,"70576;21549;3833;42277;164111;21522;93380;48471;15167;189;563;25435;87614;9696;18062;58162;10579;21681;19882;108403;128595;15582;7029"
194119823,"Adam Lewis",1444867994000,"10209"
14847001,"Adam Rogers",1422917313000,""
87709042,"Adele Green",1436867381000,"15167;18062;102811;9696;30928;18060;78565;189;7029;48471;127567;10579;58162;563;3833;16216;21441;37708;209821;15401;59325;31792;21836;21900;984862;15720;17703;96823;4422;85951;87614;37428;2260;827;121802;19672;38660;84325;118991;135612;10464;1454542;17936;21549;21520;17628;148303;20398;66339;29661"
11497937,"Adrian Bridgett",1421067940000,"30372;15046;25375;638;498;933;374;27591;18062;18060;15167;10581;16438;15672;1998;1273;713;26333;15099;15117;4422;15892;242;142180;563;31197;20479;1502;131178;15018;43256;58259;1201;7319;15940;223;8652;66493;15029;18528;23274;9696;128595;21681;17558;50709;113737"
14151190,"adrian lawrence",1437142198000,"7029;78565;659;85951;15582;48471;9696;128595;563;10579;3833;101960;16137;1973;78566;206;223;21441;16216;108403;21681;186;1998;15731;17703;15043;16613;17885;53531;48375;16615;19646;62326;49954;933;22268;19243;37381;102811;30928;455;10358;73511;127567;106382;16573;36229;781;23981;1954"
183557824,"Adrien Pujol",1421882756000,"108403;563;9696;21681;188;24410;1064;32743;124668;15472;21123;1486432;1500742;87614;46831;1454542;46810;166000;126177;110474"
...
~~~
