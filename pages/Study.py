import streamlit as st
import os

st.title('さほのえいご学習')
st.subheader(":blue[さあ、今日もがんばりましょう]")

Lesson = st.sidebar.radio('さあ英語学習！レッスンをえらんでね',
    ('Lesson1','Lesson2', 'Lesson3','Lesson4','Lesson5','Lesson6','Lesson7','Lesson8','Lesson2402','Lesson2403','Lesson2404'))

if Lesson == 'Lesson1':
    texts = {
            'Good morning':'おはよう','Good night':'おやすみ','Excuse me':'すみません','Sure':'もちろん',
            'Thank you':'ありがとう','See you tomorrow':'またあした','You are welcome':'どういたしまして',
            'Nice to meet you':'はじめまして','I am sorry':'ごめんなさい','Here you are':'はいどうぞ',
            'Have a good time':'たのしんできてね','That is good idea':'それはいいかんがえだ',
            'big':'大きい','music':'おんがく','guitar':'ギター','water':'水','small':'小さい',
            'window':'まど','piano':'ピアノ','friend':'友だち'
            }
elif Lesson == 'Lesson2':
    texts = {
            'I live in Yokohama':'ぼくは横浜に住んでいます','How about you':'あなたはどうですか',
            'I am in the soccer club':'僕はサッカークラブに入っています',
            'I am from America':'私はアメリカ出身です','What is your name':'あなたの名前は何ですか',
            'I am Yutaka':'僕はユタカです','I am from Japan':'僕は日本出身です',
            'I am eleven years old':'僕は11歳です',
            'many':'たくさん','page':'ページ','speak':'はなす','hot':'あつい','like':'すき',
            'fast':'はやい','desk':'つくえ','time':'時間','classroom':'教室','textbook':'教科書',
            'over there':'あそこで','listen to':'きく','after':'あとで','open':'ひらく',
            'sit down':'すわる','run':'走る','sunny':'晴れ','happy':'うれしい',
            'read':'読む','sing':'歌う'
            }
elif Lesson == 'Lesson3':
    texts = {
            'Do you have any comic books':'あなたはマンガの本を持っていますか',
            'Yes,I have a lot of them':'はい。私はたくさん持っています',
            'Do you know the story of Cinderella':'あなたはシンデレラの物語を知っていますか',
            'Do you have a pet?':'あなたはペットを飼っていますか','Yes,I do':'はい、飼っています',
            'No,I do not':'いいえ、飼っていません','Do you want some tea?':'あなたは紅茶がほしいですか',
            'I like chocolate ice cream':'私はチョコレートアイスクリームが好きです',
            'library':'図書館','write':'書く','know':'知っている','chair':'いす','math':'さんすう',
            'science':'科学','start':'はじめる','study':'勉強する','notebook':'ノート',
            'homework':'宿題（しゅくだい）','dictionary':'辞書（じしょ）','favorite':'だいすき',
            'magazine':'雑誌（ざっし）','a lot of':'たくさん','name':'なまえ','school':'学校（がっこう）',
            'English':'英語（えいご）','Of course':'もちろん','Me,too':'わたしも','Yes,please':'はい、お願いします'
            }
  
elif Lesson == 'Lesson4':
    texts = {
            'He is eleven years old':'私は11歳です。',
            'He is twelve years old ':'私は12歳です。',
            'Is it your guitar ':'それはあなたのギターですか。',
            'She is in the music club':'彼女は音楽クラブに入っています。',
            'Is that girl your classmate':'あの女の子はあなたのクラスメートですか？',
            'Yes Her name is Mary':'はい、彼女の名前はメアリーです。',
            'Is this a violin?':'これはヴァイオリンですか？',
            'No,it is not':'いいえ、それはちがいます。','Is it yours?':'それはあなたのものですか？',
            'No,it is my brothers':'いいえ、私の兄のものです。',
            'tennis':'テニス','basketball':'バスケットボール','baseball':'野球（やきゅう）',
            'towel':'タオル','swim':'泳ぐ（およぐ）',
            'dance':'ダンス','soccer':'サッカー','badminton':'バトミントン','gym':'ジム',
            'pool':'プール','racket':'ラケット','sport':'スポーツ',
            'volleyball':'バレーボール','well':'よく','sleep':'眠る（ねむる）','bed':'ベッド',
            'hand':'手','see':'見る','doctor':'医者（いしゃ）','hospital':'病院（びょういん）'
            }     
     
elif Lesson == 'Lesson5':
    texts = {
            'Does your father play any sports？':'あなたのお父さんは何かスポーツをしますか？',
            'He plays baseball very well.':'彼は野球がとても上手です。',
            'Does your brother play the violin?':'あなたのお兄さんはヴァイオリンを演奏しますか？',
            'No,he does not.':'いいえ、しません。',
            'My father gets up at six in the morning.':'私の父は朝6寺に起きます。',
            'Does she like music?':'彼女は音楽が好きですか？',
            'She does not like music.':'彼女は音楽が好きではありません。',
            'Does my father listen to Japanese music?':'あなたのお父さんは日本の音楽を聞きますか？',
            'next':'となりの','tall':'背が高い','mountain':'山',
            'bus':'バス','camera':'カメラ','shop':'店',
            'cold':'冷たい','jacket':'上着（うわぎ）','food':'食べ物','station':'駅（えき）',
            'get up':'起きる（おきる）','take a picture':'写真をとる','week':'1週間（1しゅうかん）',
            'Monday':'月曜日','Tuesday':'火曜日','Wednesday':'水曜日','Thursday':'木曜日',
            'Friday':'金曜日','Saturday':'土曜日','Sunday':'日曜日'
            } 
     
elif Lesson == 'Lesson6':
    texts = {
            'they are not using the computer.':'彼らはコンピュータを使っていません。',
            'I am playing the piano.':'私はピアノを引いています。',
            'what are you doing?':'あなたは何をしているのですか？',
            'I am reading a book.':'私は本を読んでいます。',
            'what are they doing?':'彼らは何をしていますか？',
            'they are looking at the birds.':'彼らは鳥を見ています。',
            'is he watching TV?':'彼はテレビを見ていますか？',
            'he is watching a baseball game.':'彼は野球の試合を見ています。',
            'February':'2月','June':'6月','night':'夜',
            'May':'5月','March':'3月','August':'8月',
            'December':'12月','month':'月','September':'9月','calendar':'カレンダー',
            'July':'7月','every　day':'毎日','November':'11月',
            'October':'10月','birthday':'誕生日','year':'年','weekend':'週末',
            'today':'今日','January':'1月','April':'4月'
            } 

elif Lesson == 'Lesson7':
    texts = {
            'I can play soccer.':'ぼくはサッカーが出来ます。',
            'can you play soccer?':'あなたはサッカーが出来ますか？',
            'I can not drink coffee.':'私はコーヒーが飲めません。',
            'can you drink coffee?':'あなたはコーヒーが飲めますか？',
            'can she run very fast?':'彼女はとても速く走ることは出来ますか？',
            'yes,she can.':'はい、出来ます。',
            'I can not have any pets.':'私はペットを飼うことが出来ません。',
            'Judy can make sandwiches very well.':'ジュディはサンドイッチを作ることがとても上手です。',
            'window':'窓（まど）','close':'閉める（しめる）','comic book':'漫画本（まんがぽん）',
            'tea':'紅茶（こうちゃ）','guitar':'ギター','before':'〜の前に',
            'bike':'自転車（じてんしゃ）','come':'来る（くる）','house':'家','make':'を作る',
            'room':'部屋','at home':'家で','bird':'鳥',
            'walk':'歩く','flower':'花','garden':'庭','wash':'を洗う',
            'morning':'朝','park':'公園','tree':'木'
            } 

elif Lesson == 'Lesson8':
    texts = {
            'How much is this shirt?':'このシャツはいくらですか？',
            'Which do you like, baseball or soccer?':'あなたは野球とサッカーどちらが好きですか？',
            'Can I have a glass of water?':'水を一杯もらえますか？',
            'How old are you?':'あなたは何歳ですか？',
            'How many books do you have?':'あなたは本を何冊持っていますか？',
            'Can you pass me ketchup?':'ケチャップを取ってもらえますか？',
            'Whose bag is this?':'これはだれのカバンですか？',
            'How do you come to school?':'あなたはどのようにして学校へ来ますか？',
            'under':'〜の下に','years old':'〜さい','fish':'魚',
            'milk':'ミルク','buy':'〜を買う','fruit':'くだもの',
            'need':'ひつようとする','supermarket':'スーパーマーケット','father':'お父さん','mother':'お母さん',
            'brother':'兄','sister':'姉','grandfather':'おじいさん',
            'grandmother':'おばあさん','sofa':'ソファー','talk about':'〜について話す','family':'家族（かぞく）',
            'live':'住む','pet':'ペット','with':'といっしょに'
            } 
 
elif Lesson == 'Lesson2402':
    texts = {
            'Where are the keys?':'カギはどこですか？',
            'They are in the box.':'箱の中です。',
            'Where is the cat?':'ネコはどこですか？',
            'It is under the chair.':'いすの下です。',
            'What sport do you like?':'何のスポーツが好きですか？',
            'What do you want for dinner tonight?':'今晩の夕食は何が食べたいですか？',
            'What is in your bag?':'あなたのかばんには何が入っていますか？',
            'How is the weather?':'お天気はどうですか？',
            'It is sunny.':'晴れています。','It is raining.':'雨が降（ふ）っています。','It is cloudy.':'曇（くも）っています。',
            'It is windy.':'風が吹（ふ）いています。','It is mine.':'私のものです。','restaurant':'レストラン',
            'hungry':'空腹（くうふく）','cup':'カップ','eat':'食べる','bread':'パン',
            'ice cream':'アイスクリーム','dinner':'夕食（ゆうしょく）','have':'持っている（もっている）',
            'lunch':'昼ごはん','want':'〜が欲しい（〜がほしい）','a glass of water':'一杯の水','in':'〜の中に',
            'on':'〜の上に','under':'〜の下に','by':'〜によって'
            }
            
elif Lesson == 'Lesson2403':
    texts = {
            'What time do you usually go to bed?':'あなたはたいてい何時に寝ますか？',
            'I go to bed at nine.':'私は9時に寝ます。',
            'What time do you get up?':'あなたは何時に起きますか？',
            'When do you study English?':'あなたはいつ英語を勉強しますか？',
            'What time is it?':'何時ですか？',
            'What day of the week is it today?':'今日は何曜日ですか？',
            'When is Keikos birthday?':'ケイコの誕生日はいつですか？',
            'It is ten oclock.':'10時です。',
            'really':'本当に','Singapore':'シンガポール','office':'会社（かいしゃ）',
            'summer':'夏','take':'〜にのる','come from':'〜出身です。',
            'computer':'コンピューター','newspaper':'新聞（しんぶん）','coffee':'コーヒー','often':'よく',
            'dollar':'ドル','a cup of tea':'一杯の紅茶（こうちゃ）','birthday':'誕生日（たんじょうび）',
            'drink':'飲む','talk':'話す','present':'プレゼント','sandwich':'サンドイッチ',
            'juice':'ジュース','people':'人々','postcard':'ハガキ' 
            } 

elif Lesson == 'Lesson2404':
    texts = {
            'Let us go to the park.':'公園へ行きましょう。',
            'Let us play badminton there.':'そこでバドミントンをしよう。',
            'We can not play badminton today.':'私たちはバドミントンが出来ません。',
            'Do not take a photo.':'写真を撮ってはいけません。',
            'Do not use your cellphone.':'携帯電話を使用してはいけません。',
            'Please do not run in the classroom.':'教室内で走らないでください。',
            'I sometimes go shopping.':'私はときどき買い物に行きます。',
            'I like eating Japanese food.':'私は日本食を食べるのが好きです。',
            'Good night':'おやすみ','Do not run here.':'ここを走らないでください。','I am sorry.':'ごめんなさい',
            'Excuse me.':'すみませんが','That is OK.':'いいよ','You are welcome.':'どういたしまして',
            'Good morning':'おはよう','Here you are.':'はい、どうぞ','Have a nice weekend.':'良い週末をお過ごしください','You too.':'あなたも',
            'Of course.':'もちろん','Nice to meet you.':'はじめまして','Welcome to our home.':'ようこそ我が家へ',
            'Breakfast is ready.':'朝食が用意できています','See you tomorrow.':'また明日','How old are you?':'あなたは何歳ですか？',
            'Who is that man?':'あの人は誰ですか？','I am coming.':'今行くよ。','How much is this magazine?':'この雑誌はいくらですか？',
            'Thank you for your help.':'助けてくれてありがとう。' 
            } 

selected = st.radio('えいご',texts,index=1,horizontal=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    onsei = st.button('発音')
with col2:
    onsei2 = st.button('発音(スロー)')
with col3:
    jp_btn = st.button('日本語')
with col4:
    sound = st.button('音を鳴らす')

if jp_btn:
    for text in texts:
        if selected == text:
            t1 = texts.get(text)
            st.write(t1) 
if onsei:
    for text in texts:
        if selected == text: 
            fil = './音声データ2/'+Lesson+'/'+text+'.mp3'
            audio_file = open(fil, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes) 
if onsei2:
    for text in texts:
        if selected == text: 
            fil2 = './音声データ_slow/'+Lesson+'/'+text+'.mp3'
            audio_file2 = open(fil2, "rb")
            audio_bytes = audio_file2.read()
            st.audio(audio_bytes) 
            #st.audio(fil2)
if sound:
    for text in texts:
        if selected == text: 
            fil3 = './音声データ2/'+Lesson+'/'+text+'.mp3'
            st.audio(fil3,format = "audio/mpeg")                 
                       
    
