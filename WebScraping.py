import requests
from bs4 import BeautifulSoup

def makale_cek(url):
    url1 = requests.get(url)
    soup = BeautifulSoup(url1.content, "lxml")
    a = ""
    for p in soup.select('article>p'):
        a = a + p.getText()
    if (a != ""):
        return a

    if a == "":
        for i in soup.select('p:not(:has(*))'):
            a = a + i.getText()

        if (a != ""):
            a = a.strip("""Haberturk.com ekibi olarak Türkiye’de ve dünyada yaşanan ve haber değeri taşıyan her türlü gelişmeyi sizlere en hızlı, en objektif ve en doyurucu şekilde ulaştırmak için çalışıyoruz. Yoğun gündem içerisinde sunduğumuz haberlerimizle ve olaylarla ilgili eleştiri, görüş, yorumlarınız bizler için çok önemli. Fakat karşılıklı saygı ve yasalara uygunluk çerçevesinde oluşturduğumuz yorum platformlarında daha sağlıklı bir tartışma ortamını temin etmek amacıyla ortaya koyduğumuz bazı yorum ve moderasyon kurallarımıza dikkatinizi çekmek istiyoruz.
            Sayfamızda Türkiye Cumhuriyeti kanunlarına ve evrensel insan haklarına aykırı yorumlar onaylanmaz ve silinir. Okurlarımız tarafından yapılan yorumların, (yorum yapan diğer okurlarımıza yönelik yorumlar da dahil olmak üzere) kişilere, ülkelere, topluluklara, sosyal sınıflara ırk, cinsiyet, din, dil başta olmak üzere ayrımcılık unsurları taşıması durumunda yorum editörlerimiz yorumları onaylamayacaktır ve yorumlar silinecektir. Onaylanmayacak ve silinecek yorumlar kategorisinde aşağılama, nefret söylemi, küfür, hakaret, kadın ve çocuk istismarı, hayvanlara yönelik şiddet söylemi içeren yorumlar da yer almaktadır. Suçu ve suçluyu övmek, Türkiye Cumhuriyeti yasalarına göre suçtur. Bu nedenle bu tarz okur yorumları da doğal olarak Haberturk.com yorum sayfalarında yer almayacaktır.
            Ayrıca Haberturk.com yorum sayfalarında Türkiye Cumhuriyeti mahkemelerinde doğruluğu ispat edilemeyecek iddia, itham ve karalama içeren, halkın tamamını veya bir bölümünü kin ve düşmanlığa tahrik eden, provokatif yorumlar da yapılamaz.
            Yorumlarda markaların ticari itibarını zedeleyici, karalayıcı ve herhangi bir şekilde ticari zarara yol açabilecek yorumlar onaylanmayacak ve silinecektir. Aynı şekilde bir markaya yönelik promosyon veya reklam amaçlı yorumlar da onaylanmayacak ve silinecek yorumlar kategorisindedir. Başka hiçbir siteden alınan linkler Haberturk.com yorum sayfalarında paylaşılamaz.
            Haberturk.com yorum sayfalarında paylaşılan tüm yorumların yasal sorumluluğu yorumu yapan okura aittir ve Haberturk.com bunlardan sorumlu tutulamaz.
            Bizlerle ve diğer okurlarımızla yorum kurallarına uygun yorumlarınızı, görüşlerinizi yasalar, saygı, nezaket, birlikte yaşama kuralları ve insan haklarına uygun şekilde paylaştığınız için teşekkür ederiz.
            Şifrenizi sıfırlamak için oturum açarken kullandığınız e-posta adresinizi giriniz""")
            return a
        if a == "":
            for j in soup.select("p"):
                a = a + j.getText()
                return a