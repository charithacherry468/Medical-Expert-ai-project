"""
All text shown on the website, in four languages:
English (en), Hindi (hi), Telugu (te), Tamil (ta).

To add a language: add it to LANGUAGES, UI, every SYMPTOMS list and DISEASES.
For SYMPTOMS, the FIRST name in each list is the one displayed; the others are
extra words the user may type (aliases).
"""

LANGUAGES = {
    "en": {"native": "English", "english": "English", "speech": "en-IN"},
    "hi": {"native": "हिन्दी", "english": "Hindi", "speech": "hi-IN"},
    "te": {"native": "తెలుగు", "english": "Telugu", "speech": "te-IN"},
    "ta": {"native": "தமிழ்", "english": "Tamil", "speech": "ta-IN"},
}

# ------------------------------------------------------------------
# Interface text
# ------------------------------------------------------------------
UI = {
    "en": {
        "title": "Medical Expert Diagnosis System",
        "check_heading": "How are you feeling today?",
        "check_sub": "Pick your symptoms below, or type them in your own words.",
        "pick_title": "Pick your symptoms",
        "search_ph": "Search symptoms...",
        "type_title": "Or type / speak your symptoms",
        "type_ph": "Example: fever, cough, body ache",
        "type_hint": "Separate symptoms with commas.",
        "mic": "Speak",
        "mic_listening": "Listening...",
        "selected": "selected",
        "diagnose": "Check my symptoms",
        "clear": "Clear",
        "err_none": "Please pick or type at least one symptom.",
        "unknown_label": "We could not understand:",
        "result_heading": "Your Result",
        "your_symptoms": "Your symptoms",
        "possible": "Possible conditions",
        "match_label": "symptoms matched",
        "matched_label": "Matched",
        "advice_label": "Advice",
        "none_found": "No likely condition found. If you still feel unwell, please see a doctor.",
        "ruled_out": "Ruled out by exception rules",
        "because": "because you also have:",
        "warning": "You selected a serious symptom. Seek medical help immediately.",
        "disclaimer": "This is an educational prototype and not a medical diagnosis. Please consult a qualified doctor.",
        "check_again": "Check again",
        "print": "Print result",
        "how": "How this works: the knowledge base is searched using unification, and default reasoning removes conditions that have exceptions.",
        "language": "Language",
    },
    "hi": {
        "title": "चिकित्सा विशेषज्ञ निदान प्रणाली",
        "check_heading": "आज आप कैसा महसूस कर रहे हैं?",
        "check_sub": "नीचे से अपने लक्षण चुनें, या अपने शब्दों में लिखें।",
        "pick_title": "अपने लक्षण चुनें",
        "search_ph": "लक्षण खोजें...",
        "type_title": "या अपने लक्षण लिखें / बोलें",
        "type_ph": "उदाहरण: बुखार, खांसी, बदन दर्द",
        "type_hint": "लक्षणों को कॉमा (,) से अलग करें।",
        "mic": "बोलें",
        "mic_listening": "सुन रहा हूँ...",
        "selected": "चुने गए",
        "diagnose": "मेरे लक्षण जांचें",
        "clear": "साफ़ करें",
        "err_none": "कृपया कम से कम एक लक्षण चुनें या लिखें।",
        "unknown_label": "हम इन्हें समझ नहीं पाए:",
        "result_heading": "आपका परिणाम",
        "your_symptoms": "आपके लक्षण",
        "possible": "संभावित रोग",
        "match_label": "लक्षण मेल खाए",
        "matched_label": "मेल खाए",
        "advice_label": "सलाह",
        "none_found": "कोई संभावित रोग नहीं मिला। फिर भी अस्वस्थ लगे तो कृपया डॉक्टर से मिलें।",
        "ruled_out": "अपवाद नियमों से बाहर किए गए",
        "because": "क्योंकि आपको यह भी है:",
        "warning": "आपने एक गंभीर लक्षण चुना है। तुरंत चिकित्सा सहायता लें।",
        "disclaimer": "यह केवल शैक्षिक प्रोटोटाइप है, चिकित्सकीय निदान नहीं। कृपया योग्य डॉक्टर से सलाह लें।",
        "check_again": "फिर से जांचें",
        "print": "परिणाम प्रिंट करें",
        "how": "यह कैसे काम करता है: ज्ञान-आधार में यूनिफ़िकेशन से मिलान किया जाता है और डिफ़ॉल्ट रीज़निंग अपवाद वाले रोगों को हटा देती है।",
        "language": "भाषा",
    },
    "te": {
        "title": "వైద్య నిపుణ నిర్ధారణ వ్యవస్థ",
        "check_heading": "ఈ రోజు మీకు ఎలా అనిపిస్తోంది?",
        "check_sub": "కింద నుండి మీ లక్షణాలను ఎంచుకోండి, లేదా మీ మాటల్లో టైప్ చేయండి.",
        "pick_title": "మీ లక్షణాలను ఎంచుకోండి",
        "search_ph": "లక్షణాలను వెతకండి...",
        "type_title": "లేదా మీ లక్షణాలను టైప్ చేయండి / చెప్పండి",
        "type_ph": "ఉదాహరణ: జ్వరం, దగ్గు, ఒళ్ళు నొప్పులు",
        "type_hint": "లక్షణాలను కామా (,) తో వేరు చేయండి.",
        "mic": "మాట్లాడండి",
        "mic_listening": "వింటున్నాను...",
        "selected": "ఎంచుకున్నవి",
        "diagnose": "నా లక్షణాలను తనిఖీ చేయండి",
        "clear": "తొలగించండి",
        "err_none": "దయచేసి కనీసం ఒక లక్షణాన్ని ఎంచుకోండి లేదా టైప్ చేయండి.",
        "unknown_label": "ఇవి మాకు అర్థం కాలేదు:",
        "result_heading": "మీ ఫలితం",
        "your_symptoms": "మీ లక్షణాలు",
        "possible": "సాధ్యమైన వ్యాధులు",
        "match_label": "లక్షణాలు సరిపోయాయి",
        "matched_label": "సరిపోయినవి",
        "advice_label": "సలహా",
        "none_found": "సాధ్యమైన వ్యాధి కనుగొనబడలేదు. అయినా అనారోగ్యంగా అనిపిస్తే దయచేసి డాక్టర్‌ను కలవండి.",
        "ruled_out": "మినహాయింపు నియమాల ద్వారా తొలగించబడినవి",
        "because": "ఎందుకంటే మీకు ఇవి కూడా ఉన్నాయి:",
        "warning": "మీరు తీవ్రమైన లక్షణాన్ని ఎంచుకున్నారు. వెంటనే వైద్య సహాయం పొందండి.",
        "disclaimer": "ఇది కేవలం విద్యా ప్రోటోటైప్, వైద్య నిర్ధారణ కాదు. దయచేసి అర్హత కలిగిన డాక్టర్‌ను సంప్రదించండి.",
        "check_again": "మళ్లీ తనిఖీ చేయండి",
        "print": "ఫలితాన్ని ప్రింట్ చేయండి",
        "how": "ఇది ఎలా పనిచేస్తుంది: నాలెడ్జ్ బేస్‌లో యూనిఫికేషన్ ద్వారా సరిపోల్చడం జరుగుతుంది, డిఫాల్ట్ రీజనింగ్ మినహాయింపులు ఉన్న వ్యాధులను తొలగిస్తుంది.",
        "language": "భాష",
    },
    "ta": {
        "title": "மருத்துவ நிபுணர் நோய் கண்டறிதல் அமைப்பு",
        "check_heading": "இன்று நீங்கள் எப்படி உணர்கிறீர்கள்?",
        "check_sub": "கீழே உங்கள் அறிகுறிகளைத் தேர்ந்தெடுக்கவும், அல்லது உங்கள் சொற்களில் எழுதவும்.",
        "pick_title": "உங்கள் அறிகுறிகளைத் தேர்ந்தெடுக்கவும்",
        "search_ph": "அறிகுறிகளைத் தேடுங்கள்...",
        "type_title": "அல்லது உங்கள் அறிகுறிகளை எழுதுங்கள் / பேசுங்கள்",
        "type_ph": "எடுத்துக்காட்டு: காய்ச்சல், இருமல், உடல் வலி",
        "type_hint": "அறிகுறிகளை காற்புள்ளி (,) கொண்டு பிரிக்கவும்.",
        "mic": "பேசுங்கள்",
        "mic_listening": "கேட்கிறேன்...",
        "selected": "தேர்ந்தெடுத்தவை",
        "diagnose": "என் அறிகுறிகளைச் சரிபார்",
        "clear": "அழி",
        "err_none": "குறைந்தது ஒரு அறிகுறியைத் தேர்ந்தெடுக்கவும் அல்லது எழுதவும்.",
        "unknown_label": "இவற்றை எங்களால் புரிந்துகொள்ள முடியவில்லை:",
        "result_heading": "உங்கள் முடிவு",
        "your_symptoms": "உங்கள் அறிகுறிகள்",
        "possible": "சாத்தியமான நோய்கள்",
        "match_label": "அறிகுறிகள் பொருந்தின",
        "matched_label": "பொருந்தியவை",
        "advice_label": "ஆலோசனை",
        "none_found": "சாத்தியமான நோய் எதுவும் கிடைக்கவில்லை. இருந்தாலும் உடல்நலக்குறைவு தொடர்ந்தால் மருத்துவரைப் பாருங்கள்.",
        "ruled_out": "விதிவிலக்கு விதிகளால் நீக்கப்பட்டவை",
        "because": "ஏனெனில் உங்களுக்கு இதுவும் உள்ளது:",
        "warning": "நீங்கள் தீவிரமான அறிகுறியைத் தேர்ந்தெடுத்துள்ளீர்கள். உடனடியாக மருத்துவ உதவியை நாடுங்கள்.",
        "disclaimer": "இது கல்விக்கான முன்மாதிரி மட்டுமே, மருத்துவ நோயறிதல் அல்ல. தகுதியான மருத்துவரை அணுகுங்கள்.",
        "check_again": "மீண்டும் சரிபார்",
        "print": "முடிவை அச்சிடு",
        "how": "இது எப்படி செயல்படுகிறது: அறிவுத் தளத்தில் யூனிஃபிகேஷன் மூலம் பொருத்தம் பார்க்கப்படுகிறது; டிஃபால்ட் ரீசனிங் விதிவிலக்குகள் உள்ள நோய்களை நீக்குகிறது.",
        "language": "மொழி",
    },
}

# ------------------------------------------------------------------
# Symptoms: first name = displayed name, rest = words users may type
# ------------------------------------------------------------------
SYMPTOMS = {
    "fever": {
        "en": ["Fever", "Temperature"],
        "hi": ["बुखार", "ज्वर"],
        "te": ["జ్వరం"],
        "ta": ["காய்ச்சல்"],
    },
    "high_fever": {
        "en": ["High Fever", "Very high fever"],
        "hi": ["तेज़ बुखार", "तेज बुखार"],
        "te": ["తీవ్రమైన జ్వరం", "ఎక్కువ జ్వరం"],
        "ta": ["அதிக காய்ச்சல்", "கடுமையான காய்ச்சல்"],
    },
    "cough": {
        "en": ["Cough"],
        "hi": ["खांसी", "खाँसी"],
        "te": ["దగ్గు"],
        "ta": ["இருமல்"],
    },
    "sneezing": {
        "en": ["Sneezing", "Sneeze"],
        "hi": ["छींक आना", "छींक"],
        "te": ["తుమ్ములు", "తుమ్ము"],
        "ta": ["தும்மல்"],
    },
    "runny_nose": {
        "en": ["Runny Nose", "Running nose"],
        "hi": ["बहती नाक", "नाक बहना"],
        "te": ["ముక్కు కారడం", "ముక్కు కారుట"],
        "ta": ["மூக்கு ஒழுகுதல்", "மூக்கு ஒழுகல்"],
    },
    "sore_throat": {
        "en": ["Sore Throat", "Throat pain"],
        "hi": ["गले में खराश", "गले में दर्द"],
        "te": ["గొంతు నొప్పి"],
        "ta": ["தொண்டை வலி"],
    },
    "headache": {
        "en": ["Headache", "Head ache"],
        "hi": ["सिरदर्द", "सिर दर्द", "सिर में दर्द"],
        "te": ["తలనొప్పి", "తల నొప్పి"],
        "ta": ["தலைவலி", "தலை வலி"],
    },
    "body_ache": {
        "en": ["Body Ache", "Body pain", "Body aches"],
        "hi": ["बदन दर्द", "शरीर में दर्द", "बदन में दर्द"],
        "te": ["ఒళ్ళు నొప్పులు", "ఒళ్లు నొప్పులు", "ఒంటి నొప్పులు"],
        "ta": ["உடல் வலி", "உடல்வலி"],
    },
    "joint_pain": {
        "en": ["Joint Pain"],
        "hi": ["जोड़ों का दर्द", "जोड़ों में दर्द"],
        "te": ["కీళ్ల నొప్పులు", "కీళ్ల నొప్పి"],
        "ta": ["மூட்டு வலி"],
    },
    "fatigue": {
        "en": ["Fatigue", "Tiredness", "Tired"],
        "hi": ["थकान", "थकावट"],
        "te": ["అలసట", "నీరసం"],
        "ta": ["சோர்வு", "களைப்பு"],
    },
    "chills": {
        "en": ["Chills", "Shivering"],
        "hi": ["ठंड लगना", "कंपकंपी"],
        "te": ["చలి", "వణుకు"],
        "ta": ["குளிர்", "குளிர் நடுக்கம்"],
    },
    "sweating": {
        "en": ["Sweating"],
        "hi": ["पसीना आना", "पसीना"],
        "te": ["చెమట", "చెమటలు"],
        "ta": ["வியர்வை"],
    },
    "nausea": {
        "en": ["Nausea"],
        "hi": ["मतली", "जी मिचलाना"],
        "te": ["వికారం"],
        "ta": ["குமட்டல்"],
    },
    "vomiting": {
        "en": ["Vomiting", "Vomit"],
        "hi": ["उल्टी", "उलटी"],
        "te": ["వాంతులు", "వాంతి"],
        "ta": ["வாந்தி"],
    },
    "diarrhea": {
        "en": ["Diarrhea", "Diarrhoea", "Loose motions"],
        "hi": ["दस्त", "पतले दस्त"],
        "te": ["విరేచనాలు"],
        "ta": ["வயிற்றுப்போக்கு"],
    },
    "constipation": {
        "en": ["Constipation"],
        "hi": ["कब्ज़", "कब्ज"],
        "te": ["మలబద్ధకం"],
        "ta": ["மலச்சிக்கல்"],
    },
    "abdominal_pain": {
        "en": ["Abdominal Pain", "Stomach pain", "Stomach ache"],
        "hi": ["पेट दर्द", "पेट में दर्द"],
        "te": ["కడుపు నొప్పి", "కడుపునొప్పి"],
        "ta": ["வயிற்று வலி"],
    },
    "loss_of_appetite": {
        "en": ["Loss of Appetite", "No appetite"],
        "hi": ["भूख न लगना", "भूख कम लगना"],
        "te": ["ఆకలి లేకపోవడం", "ఆకలి వేయకపోవడం"],
        "ta": ["பசியின்மை"],
    },
    "eye_pain": {
        "en": ["Eye Pain"],
        "hi": ["आंख में दर्द", "आँख में दर्द"],
        "te": ["కంటి నొప్పి"],
        "ta": ["கண் வலி"],
    },
    "rash": {
        "en": ["Rash", "Skin rash"],
        "hi": ["चकत्ते", "दाने", "त्वचा पर दाने"],
        "te": ["దద్దుర్లు", "దద్దురు"],
        "ta": ["தோல் தடிப்பு", "சொறி"],
    },
    "breathing_difficulty": {
        "en": ["Breathing Difficulty", "Shortness of breath", "Breathless"],
        "hi": ["सांस लेने में तकलीफ", "सांस फूलना"],
        "te": ["శ్వాస తీసుకోవడంలో ఇబ్బంది", "ఊపిరి ఆడకపోవడం"],
        "ta": ["சுவாசிக்க சிரமம்", "மூச்சுத் திணறல்"],
    },
    "chest_pain": {
        "en": ["Chest Pain"],
        "hi": ["सीने में दर्द", "छाती में दर्द"],
        "te": ["ఛాతీ నొప్పి", "ఛాతి నొప్పి"],
        "ta": ["மார்பு வலி", "நெஞ்சு வலி"],
    },
    "confusion": {
        "en": ["Confusion"],
        "hi": ["भ्रम", "उलझन"],
        "te": ["గందరగోళం"],
        "ta": ["குழப்பம்"],
    },
}

# Order in which symptom chips are shown (common ones first)
SYMPTOM_ORDER = [
    "fever", "high_fever", "cough", "sneezing", "runny_nose", "sore_throat",
    "headache", "body_ache", "joint_pain", "fatigue", "chills", "sweating",
    "nausea", "vomiting", "diarrhea", "constipation", "abdominal_pain",
    "loss_of_appetite", "eye_pain", "rash", "breathing_difficulty",
    "chest_pain", "confusion",
]

SYMPTOM_EMOJI = {
    "fever": "🤒", "high_fever": "🌡️", "cough": "😷", "sneezing": "🤧",
    "runny_nose": "💧", "sore_throat": "🗣️", "headache": "🤕",
    "body_ache": "💪", "joint_pain": "🦴", "fatigue": "😴", "chills": "🥶",
    "sweating": "💦", "nausea": "🤢", "vomiting": "🤮", "diarrhea": "🚽",
    "constipation": "😖", "abdominal_pain": "😣", "loss_of_appetite": "🍽️",
    "eye_pain": "👁️", "rash": "🔴", "breathing_difficulty": "🌬️",
    "chest_pain": "💔", "confusion": "😵",
}

# ------------------------------------------------------------------
# Diseases: name and general advice (no dosages)
# ------------------------------------------------------------------
DISEASES = {
    "common_cold": {
        "emoji": "🤧",
        "en": {"name": "Common Cold",
               "advice": "Rest, warm fluids, steam inhalation."},
        "hi": {"name": "सामान्य सर्दी-जुकाम",
               "advice": "आराम करें, गुनगुने तरल पदार्थ लें और भाप लें।"},
        "te": {"name": "సాధారణ జలుబు",
               "advice": "విశ్రాంతి తీసుకోండి, గోరువెచ్చని ద్రవాలు తాగండి, ఆవిరి పట్టండి."},
        "ta": {"name": "சாதாரண சளி",
               "advice": "ஓய்வெடுங்கள், வெதுவெதுப்பான பானங்கள் குடியுங்கள், ஆவி பிடியுங்கள்."},
    },
    "flu": {
        "emoji": "🤒",
        "en": {"name": "Flu (Influenza)",
               "advice": "Rest, plenty of fluids; take fever relief only as advised by a doctor."},
        "hi": {"name": "फ्लू (इन्फ्लुएंजा)",
               "advice": "आराम करें, खूब पानी और तरल पदार्थ पिएं; बुखार की दवा केवल डॉक्टर की सलाह से लें।"},
        "te": {"name": "ఫ్లూ (ఇన్‌ఫ్లుయెంజా)",
               "advice": "విశ్రాంతి తీసుకోండి, ఎక్కువ ద్రవాలు తాగండి; జ్వరం మందులు డాక్టర్ సలహాతో మాత్రమే వాడండి."},
        "ta": {"name": "காய்ச்சல் (இன்ஃப்ளூயன்சா)",
               "advice": "ஓய்வெடுங்கள், நிறைய திரவங்கள் குடியுங்கள்; காய்ச்சல் மருந்துகளை மருத்துவர் ஆலோசனைப்படி மட்டுமே எடுத்துக்கொள்ளுங்கள்."},
    },
    "malaria": {
        "emoji": "🦟",
        "en": {"name": "Malaria",
               "advice": "Needs a blood test and prescribed medicine. See a doctor."},
        "hi": {"name": "मलेरिया",
               "advice": "रक्त जांच और डॉक्टर द्वारा बताई दवा आवश्यक है। डॉक्टर से मिलें।"},
        "te": {"name": "మలేరియా",
               "advice": "రక్త పరీక్ష మరియు డాక్టర్ సూచించిన మందులు అవసరం. డాక్టర్‌ను కలవండి."},
        "ta": {"name": "மலேரியா",
               "advice": "இரத்தப் பரிசோதனையும் மருத்துவர் பரிந்துரைத்த மருந்தும் தேவை. மருத்துவரைப் பாருங்கள்."},
    },
    "dengue": {
        "emoji": "🩸",
        "en": {"name": "Dengue",
               "advice": "Needs a blood test. Rest and fluids; see a doctor for monitoring."},
        "hi": {"name": "डेंगू",
               "advice": "रक्त जांच आवश्यक है। आराम करें और तरल पदार्थ लें; निगरानी के लिए डॉक्टर से मिलें।"},
        "te": {"name": "డెంగ్యూ",
               "advice": "రక్త పరీక్ష అవసరం. విశ్రాంతి, ద్రవాలు తీసుకోండి; పర్యవేక్షణ కోసం డాక్టర్‌ను కలవండి."},
        "ta": {"name": "டெங்கு",
               "advice": "இரத்தப் பரிசோதனை தேவை. ஓய்வு, திரவங்கள் எடுத்துக்கொள்ளுங்கள்; கண்காணிப்புக்கு மருத்துவரைப் பாருங்கள்."},
    },
    "typhoid": {
        "emoji": "🧫",
        "en": {"name": "Typhoid",
               "advice": "Needs a lab test and prescribed antibiotics. See a doctor."},
        "hi": {"name": "टाइफाइड",
               "advice": "प्रयोगशाला जांच और डॉक्टर द्वारा बताए एंटीबायोटिक आवश्यक हैं। डॉक्टर से मिलें।"},
        "te": {"name": "టైఫాయిడ్",
               "advice": "ల్యాబ్ పరీక్ష మరియు డాక్టర్ సూచించిన యాంటీబయాటిక్స్ అవసరం. డాక్టర్‌ను కలవండి."},
        "ta": {"name": "டைபாய்டு",
               "advice": "ஆய்வகப் பரிசோதனையும் மருத்துவர் பரிந்துரைத்த நுண்ணுயிர்க்கொல்லி மருந்தும் தேவை. மருத்துவரைப் பாருங்கள்."},
    },
    "gastroenteritis": {
        "emoji": "🤢",
        "en": {"name": "Gastroenteritis (Stomach Infection)",
               "advice": "Oral rehydration, light food; see a doctor if it lasts long."},
        "hi": {"name": "गैस्ट्रोएंटेराइटिस (पेट का संक्रमण)",
               "advice": "ओआरएस (मौखिक पुनर्जलीकरण) लें, हल्का भोजन करें; लंबे समय तक रहे तो डॉक्टर से मिलें।"},
        "te": {"name": "గ్యాస్ట్రోఎంటెరైటిస్ (కడుపు ఇన్ఫెక్షన్)",
               "advice": "ఓఆర్ఎస్ ద్రావణం తాగండి, తేలికపాటి ఆహారం తీసుకోండి; ఎక్కువ రోజులు ఉంటే డాక్టర్‌ను కలవండి."},
        "ta": {"name": "இரைப்பை குடல் அழற்சி (வயிற்றுத் தொற்று)",
               "advice": "ORS கரைசல் குடியுங்கள், இலகுவான உணவு சாப்பிடுங்கள்; நீண்ட நாட்கள் நீடித்தால் மருத்துவரைப் பாருங்கள்."},
    },
}


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def sname(symptom_id, lang):
    """Display name of a symptom in the chosen language."""
    return SYMPTOMS[symptom_id][lang][0]


def search_text(symptom_id):
    """All names in all languages, lowercase, used by the search box."""
    names = []
    for lang_names in SYMPTOMS[symptom_id].values():
        names.extend(lang_names)
    return " ".join(names).lower()
