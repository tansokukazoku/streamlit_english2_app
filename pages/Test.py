import streamlit as st
from playsound import playsound
from PIL import Image


st.title('英語テスト')
st.subheader(":blue[テストです。間違えたら問題にもどりましょう！]")

Lesson = st.sidebar.radio('さあテストに挑戦！レッスンをえらんでね',
        ('Lesson1','Lesson2', 'Lesson3','Lesson4','Lesson5','Lesson6','Lesson7','Lesson8','Lesson2402','Lesson2403','Lesson2404'))

if Lesson == 'Lesson1':
    texts = {
                'おはよう':'Good morning','おやすみ':'Good night','すみません':'Excuse me','もちろん':'Sure',
                'ありがとう':'Thank you','またあした':'See you tomorrow','どういたしまして':'You are welcome',
                'はじめまして':'Nice to meet you','ごめんなさい':'I am sorry','はいどうぞ':'Here you are',
                'たのしんできてね':'Have a good time','それはいいかんがえだ':'That is good idea'
                }
elif Lesson == 'Lesson2':
    texts = {
            'ぼくは横浜に住んでいます':'I live in Yokohama',
            'あなたはどうですか':'How about you',
            '僕はサッカークラブに入っています':'I am in the soccer club',
            '私はアメリカ出身です':'I am from America',
            'あなたの名前は何ですか':'What is your name',
            '僕はユタカです':'I am Yutaka',
            '僕は日本出身です':'I am from Japan',
            '僕は11歳です':'I am eleven years old'
            }
    test2_1 =('I live Yokohama in','I live in Yokohama','live I in Yokohama')
    test2_2 =('you How about','How you about','How about you')
    test2_3 =('I am in soccer the club','I am the soccer in club','I am in the soccer club')
    test2_4 =('I am from America','am I from America','I am America from')
    test2_5 =('What your name is','What is name your','What is your name')
    test2_6 =('am I Yutaka','I am Yutaka','I Yutaka am')
    test2_7 =('I am from Japan','I from am Japan','am I from Japan')
    test2_8 =('I am eleven years old','I am eleven old years','am I eleven years old')
    tests = {
            'ぼくは横浜に住んでいます':test2_1,
            'あなたはどうですか':test2_2,
            '僕はサッカークラブに入っています':test2_3,
            '私はアメリカ出身です':test2_4,
            'あなたの名前は何ですか':test2_5,
            '僕はユタカです':test2_6,
            '僕は日本出身です':test2_7,
            '僕は11歳です':test2_8,
            }
elif Lesson == 'Lesson3':
    texts = {
            'あなたはマンガの本を持っていますか':'Do you have any comic books',
            'はい。私はたくさん持っています':'Yes,I have a lot of them',
            'あなたはシンデレラの物語を知っていますか':'Do you know the story of Cinderella',
            'あなたはペットを飼っていますか':'Do you have a pet?',
            'はい、飼っています':'Yes,I do',
            'いいえ、飼っていません':'No,I do not',
            'あなたは紅茶がほしいですか':'Do you want some tea?',
            '私はチョコレートアイスクリームが好きです':'I like chocolate ice cream'
            }
    test3_1 =('Do you have comic any books','Do you have any comic books','Do you have books any comic')
    test3_2 =('Yes,I have a lot of them','Yes,I have a lot them of','Yes,I have lot a of them')
    test3_3 =('Do you know the story of Cinderella','Do you know the Cinderella story of','Do you know of the Cinderella story')
    test3_4 =('Do you have pet a?','Do have you a pet?','Do you have a pet?')
    test3_5 =('do Yes,I','Yes,do I','Yes,I do')
    test3_6 =('No,I do not','No,do I not','No,I not do')
    test3_7 =('Do you want some tea?','Do you want tea some?','Do you some tea want?')
    test3_8 =('I like chocolate ice cream','I like ice chocolate cream','I chocolate ice cream like')
    tests = {
            'あなたはマンガの本を持っていますか':test3_1,
            'はい。私はたくさん持っています':test3_2,
            'あなたはシンデレラの物語を知っていますか':test3_3,
            'あなたはペットを飼っていますか':test3_4,
            'はい、飼っています':test3_5,
            'いいえ、飼っていません':test3_6,
            'あなたは紅茶がほしいですか':test3_7,
            '私はチョコレートアイスクリームが好きです':test3_8,
            }
    
elif Lesson == 'Lesson4':
    texts = {
            '私は11歳です。':'He is eleven years old',
            '私は12歳です。':'He is twelve years old ',
            'それはあなたのギターですか。':'Is it your guitar ',
            '彼女は音楽クラブに入っています。':'She is in the music club',
            'あの女の子はあなたのクラスメートですか？':'Is that girl your classmate',
            'はい、彼女の名前はメアリーです。':'Yes Her name is Mary',
            'これはヴァイオリンですか？':'Is this a violin?',
            'いいえ、それはちがいます。':'No,it is not','それはあなたのものですか？':'Is it yours?',
            'いいえ、私の兄のものです。':'No,it is my brothers'
            } 
    test4_1 =('He years is eleven old','He is eleven old years','He is eleven years old')
    test4_2 =('He is old twelve years','He years is twelve old','He is twelve years old')
    test4_3 =('it Is your guitar','Is it your guitar','Is it guitar your')
    test4_4 =('She is club in the music','She is in the music club','She is music in the club')
    test4_5 =('that Is girl your classmate','Is that girl your classmate','Is girl that your classmate')
    test4_6 =('Yes Her name is Mary','Yes Her is name Mary','Her name is Mary Yes')
    test4_7 =('this Is a violin?','Is this a violin?','Is a this violin?')
    test4_8 =('No,it not is','No,it is not','not,it is No')
    test4_9 =('No,it is my brothers','No,is it my brothers','No,it is brothers my') 
    tests = {
            '私は11歳です。':test4_1,
            '私は12歳です。':test4_2,
            'それはあなたのギターですか。':test4_3,
            '彼女は音楽クラブに入っています。':test4_4,
            'あの女の子はあなたのクラスメートですか？':test4_5,
            'はい、彼女の名前はメアリーです。':test4_6,
            'これはヴァイオリンですか？':test4_7,
            'いいえ、それはちがいます。':test4_8,
            'いいえ、私の兄のものです。':test4_9,
            }   
        
elif Lesson == 'Lesson5':
    texts = {
            'あなたのお父さんは何かスポーツをしますか？':'does your father play any sports？',
            '彼は野球がとても上手です。':'he plays baseball very well.',
            'あなたのお兄さんはヴァイオリンを演奏しますか？':'does your brother play the violin?',
            'いいえ、しません。':'no,he does not.',
            '私の父は朝6時に起きます。':'my father gets up at six in the morning.',
            '彼女は音楽が好きですか？':'does she like music?',
            '彼女は音楽が好きではありません。':'she does not like music.',
            'あなたのお父さんは日本の音楽を聞きますか？':'does my father listen to Japanese music?'
            } 
    test5_1 =('does father play your any sports','father does your play any sports','does your father play any sports？')
    test5_2 =('he baseball plays very well.','he plays baseball very well.','he plays very baseball well.')
    test5_3 =('does brother your play the violin?','does your brother play the violin?','your brother does play the violin?')
    test5_4 =('no,does he not.','no,he does not.','does he no not.')
    test5_5 =('my father gets up at six in the morning.','father gets up my six the morining does in.','my father gets up in six at the morning.')
    test5_6 =('does she like music?','she does like music?','does she music like?')
    test5_7 =('does she not like music.','she does not like music.','she like does not music.')
    test5_8 =('does my father listen to Japanese music?','my father does listen to Japanese music?','does my father Japanese listen to music?')
    tests = {'あなたのお父さんは何かスポーツをしますか？':test5_1,
                '彼は野球がとても上手です。':test5_2,
                'あなたのお兄さんはヴァイオリンを演奏しますか？':test5_3,
                'いいえ、しません。':test5_4,
                '私の父は朝6時に起きます。':test5_5,
                '彼女は音楽が好きですか？':test5_6,
                '彼女は音楽が好きではありません。':test5_6,
                '彼女は音楽が好きではありません。':test5_7,
                'あなたのお父さんは日本の音楽を聞きますか？':test5_8}
        
elif Lesson == 'Lesson6':
    texts = {
            '彼らはコンピュータを使っていません。':'they are not using the computer.',
            '私はピアノを引いています。':'I am playing the piano.',
            'あなたは何をしているのですか？':'what are you doing?',
            '私は本を読んでいます。':'I am reading a book.',
            '彼らは何をしていますか？':'what are they doing?',
            '彼らは鳥を見ています。':'they are looking at the birds.',
            '彼はテレビを見ていますか？':'is he watching TV?',
            '彼は野球の試合を見ています。':'he is watching a baseball game.'
            } 
    test6_1 =('are they not using the computer','they are not using the computer.','they are using not the computer')
    test6_2 =('am I playing the piano.','I am the playing  piano.','I am playing the piano.')
    test6_3 =('what are you doing?','what are doing you ?','what you are doing?')
    test6_4 =('I am a reading  book.','I am reading a book.','I reading am  a book.')
    test6_5 =('what are they doing?','what are doing they ?','what they are doing?')
    test6_6 =('they looking are at the birds.','they are looking the at birds.','they are looking at the birds.')
    test6_7 =('is he TV watching ?.','is he watching TV?','he is watching TV?')
    test6_8 =('he is a watching baseball game.','he is watching a baseball game.','he is watching a game baseball.')
    tests = {'彼らはコンピュータを使っていません。':test6_1,
                '私はピアノを引いています。':test6_2,
                'あなたは何をしているのですか？':test6_3,
                '私は本を読んでいます。':test6_4,
                '彼らは何をしていますか？':test6_5,
                '彼らは鳥を見ています。':test6_6,
                '彼はテレビを見ていますか？':test6_7,
                '彼は野球の試合を見ています。':test6_8}  

elif Lesson == 'Lesson7':
    texts = {
            'ぼくはサッカーが出来ます。':'I can play soccer.',
            'あなたはサッカーが出来ますか？':'can you play soccer?',
            '私はコーヒーが飲めません。':'I can not drink coffee.',
            'あなたはコーヒーが飲めますか？':'can you drink coffee?',
            '彼女はとても速く走ることは出来ますか？':'can she run very fast?',
            'はい、出来ます。':'yes,she can.',
            '私はペットを飼うことが出来ません。':'I can not have any pets.',
            'ジュディはサンドイッチを作ることがとても上手です。':'Judy can make sandwiches very well.'
            } 
    test7_1 =('can I play soccer.','I can play soccer.','I play can soccer.')
    test7_2 =('can you play soccer?','can you soccer play?','you can play soccer?')
    test7_3 =('I can  drink not coffee.','I can not drink coffee.','I can not coffee drink.')
    test7_4 =('can you drink coffee?','you can drink coffee?','can drink you coffee?')
    test7_5 =('can she fast run very?','can she very run fast?','can she run very fast?')
    test7_6 =('she can,yes.','yes,she can.','yes,can she.')
    test7_7 =('I can have not any pets.','I can not any have pets.','I can not have any pets.')
    test7_8 =('Judy make can sandwiches very well.','Judy can make very sandwiches well.','Judy can make sandwiches very well.')
    tests = {'ぼくはサッカーが出来ます。':test7_1,
                'あなたはサッカーが出来ますか？':test7_2,
                '私はコーヒーが飲めません。':test7_3,
                'あなたはコーヒーが飲めますか？':test7_4,
                '彼女はとても速く走ることは出来ますか？':test7_5,
                'はい、出来ます。':test7_6,
                '私はペットを飼うことが出来ません。':test7_7,
                'ジュディはサンドイッチを作ることがとても上手です。':test7_8} 
    
elif Lesson == 'Lesson8':
    texts = {
            'このシャツはいくらですか？':'How much is this shirt?',
            'あなたは野球とサッカーどちらが好きですか？':'Which do you like, baseball or soccer?',
            '水を一杯もらえますか？':'Can I have a glass of water?',
            'あなたは何歳ですか？':'How old are you?',
            'あなたは本を何冊持っていますか？':'How many books do you have?',
            'ケチャップを取ってもらえますか？':'Can you pass me ketchup?',
            'これはだれのカバンですか？':'Whose bag is this?',
            'あなたはどのようにして学校へ来ますか？':'How do you come to school?'
            } 
    test8_1 =('How much this shirt is ?','How much shirt is this?','How much is this shirt?')
    test8_2 =('do you Which like, baseball or soccer?','Which do you baseball, or soccer like?','Which do you like, baseball or soccer?')
    test8_3 =('Can I have a water glass of ?','Can I have a glass of water?','I Can have a glass of water?')
    test8_4 =('How old are you?','How are you old?','How old you are?')
    test8_5 =('How many you do have books?','How many do you have books?','How many books do you have?')
    test8_6 =('Can you pass ketchup me?','you Can pass me ketchup?','Can you pass me ketchup?')
    test8_7 =('Whose is bag this?','Whose is this bag?','Whose bag is this?')
    test8_8 =('How do you come to school?','How you do come to school?','How do you come school to?')
    tests = {   'このシャツはいくらですか？':test8_1,
                'あなたは野球とサッカーどちらが好きですか？':test8_2,
                '水を一杯もらえますか？':test8_3,
                'あなたは何歳ですか？':test8_4,
                'あなたは本を何冊持っていますか？':test8_5,
                'ケチャップを取ってもらえますか？':test8_6,
                'これはだれのカバンですか？':test8_7,
                'あなたはどのようにして学校へ来ますか？':test8_8}
elif Lesson == 'Lesson2402':
    texts = {
            'カギはどこですか？':'Where are the keys?',
            '箱の中です。':'They are in the box.',
            'ネコはどこですか？':'Where is the cat?',
            'いすの下です。':'It is under the chair.',
            '何のスポーツが好きですか？':'What sport do you like?',
            '今晩の夕食は何が食べたいですか？':'What do you want for dinner tonight?',
            'あなたのかばんには何が入っていますか？':'What is in your bag?',
            'お天気はどうですか？':'How is the weather?'
            } 
    test2402_1 =('Where keys are the?','Where are the keys?','Where the keys are?')
    test2402_2 =('They the box are in.','They are the in box.','They are in the box.')
    test2402_3 =('Where the cat is?','Where cat is the?','Where is the cat?')
    test2402_4 =('It chair is the under.','It is under the chair.','It is the under chair.')
    test2402_5 =('What do you sport like?','What do you like sport?','What sport do you like?')
    test2402_6 =('What do you want for dinner tonight?','What dinner do you want for tonight?','What do you want dinner for tonight?')
    test2402_7 =('What is your bag in?','What is in your bag?','What is your in bag?')
    test2402_8 =('How the weather is?','How weather is the?','How is the weather?')
    tests = {   'カギはどこですか？':test2402_1,
                '箱の中です。':test2402_2,
                'ネコはどこですか？':test2402_3,
                'いすの下です。':test2402_4,
                '何のスポーツが好きですか？':test2402_5,
                '今晩の夕食は何が食べたいですか？':test2402_6,
                'あなたのかばんには何が入っていますか？':test2402_7,
                'お天気はどうですか？':test2402_8}
    
elif Lesson == 'Lesson2403':
    texts = {
            'あなたはたいてい何時に寝ますか？':'What time do you usually go to bed?',
            '私は9時に寝ます。':'I go to bed at nine.',
            'あなたは何時に起きますか？':'What time do you get up?',
            'あなたはいつ英語を勉強しますか？':'When do you study English?',
            '何時ですか？':'What time is it?',
            '今日は何曜日ですか？':'What day of the week is it today?',
            'ケイコの誕生日はいつですか？':'When is Keikos birthday?',
            '10時です。':'It is ten oclock.'
            } 
    test2402_1 =('What time do you go usually to bed?','What do you usually go to bed time?','What time do you usually go to bed?')
    test2402_2 =('I go bed to at nine.','I go to bed at nine.','I go to at bed nine.')
    test2402_3 =('What do you get time up?','What do you get up time?','What time do you get up?')
    test2402_4 =('When you study English do?','When do you study English?','When you study do English?')
    test2402_5 =('What time is it?','What is it time?','What time it is?')
    test2402_6 =('What day is it today of the week?','What day is it of today the week?','What day of the week is it today?')
    test2402_7 =('When is Keikos birthday?','When Keikos is birthday?','When birthday is Keikos?')
    test2402_8 =('It oclock is ten.','It is ten oclock.','Is it ten oclock.')
    tests = {   
             'あなたはたいてい何時に寝ますか？':test2402_1,
             '私は9時に寝ます。':test2402_2,
             'あなたは何時に起きますか？':test2402_3,
             'あなたはいつ英語を勉強しますか？':test2402_4,
             '何時ですか？':test2402_5,
             '今日は何曜日ですか？':test2402_6,
             'ケイコの誕生日はいつですか？':test2402_7,
             '10時です。':test2402_8
            }

elif Lesson == 'Lesson2404':
    texts = {
            '公園へ行きましょう。':'Let us go to the park.',
            'そこでバドミントンをしよう。':'Let us play badminton there.',
            '私たちはバドミントンが出来ません。':'We can not play badminton today.',
            '写真を撮ってはいけません。':'Do not take a photo.',
            '携帯電話を使用してはいけません。':'Do not use your cellphone.',
            '教室内で走らないでください。':'Please do not run in the classroom.',
            '私はときどき買い物に行きます。':'I sometimes go shopping.',
            '私は日本食を食べるのが好きです。':'I like eating Japanese food.'
            } 
    test2404_1 =('Let us the go to park.','Let us go to the park.','Let us go the park to.')
    test2404_2 =('Let us play there badminton.','Let us play there badminton.','Let us play badminton there.')
    test2404_3 =('We can not play badminton today.','We can not play today badminton.','We can play not badminton today.')
    test2404_4 =('Do not take photo a.','Do not take a photo.','Do not a take photo.')
    test2404_5 =('Do not use cellphone your.','Do not your use cellphone.','Do not use your cellphone.')
    test2404_6 =('Please do not run in the classroom.','Please do not run the in classroom.','Please do not in the classroom run.')
    test2404_7 =('I go shopping sometimes.','I go sometimes shopping.','I sometimes go shopping.')
    test2404_8 =('I like Japanese food eating.','I eating like Japanese food.','I like eating Japanese food.')
    tests = {   
             '公園へ行きましょう。':test2404_1,
             'そこでバドミントンをしよう。':test2404_2,
             '私たちはバドミントンが出来ません。':test2404_3,
             '写真を撮ってはいけません。':test2404_4,
             '教室内で走らないでください。':test2404_5,
             '教室内で走らないでください。':test2404_6,
             '私はときどき買い物に行きます。':test2404_7,
             '私は日本食を食べるのが好きです。':test2404_8
            } 
                    
selected = st.radio('テスト問題',texts,index=1,horizontal=True)

col1,col2 = st.columns(2)

with col1:
    for text in texts:
            if selected == text:
                for test in tests:
                    if text == test:
                        t2 = tests.get(test)
                        kaito_hyouji = st.radio('正しい並びのえいごをえらんでから決定ボタンを押してね!!',t2)
                        
    kettei_btn = st.button('決定')

with col2:
    if kettei_btn:
        st.write('回答は:',kaito_hyouji)

        for text in texts:
            if selected == text:
                t3 = texts.get(text)
                st.write('正解は:',t3) 
                if kaito_hyouji == t3:
                    img1 = Image.open('./data/正解.png')
                    st.image(img1,width=300)
                    playsound('./data/Buzzer_seikai.mp3')
                else:
                    img2 = Image.open('./data/不正解.png')
                    st.image(img2,width=300)
                    playsound('./data/Buzzer_fuseikai.mp3')
                        
                
                
                
