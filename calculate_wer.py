# from difflib import SequenceMatcher

# def calculate_wer(original, transcribed):
#     # Tokenize the sentences into words
#     original_words = original.split()
#     transcribed_words = transcribed.split()

#     # Find the longest common subsequence
#     matcher = SequenceMatcher(None, original_words, transcribed_words)
#     matches = matcher.get_matching_blocks()

#     # Calculate substitutions, deletions, and insertions
#     substitutions = deletions = insertions = 0
#     original_index = transcribed_index = 0

#     for match in matches:
#         while original_index < match.a or transcribed_index < match.b:
#             if original_index < match.a and transcribed_index < match.b:
#                 substitutions += 1
#                 original_index += 1
#                 transcribed_index += 1
#             elif original_index < match.a:
#                 deletions += 1
#                 original_index += 1
#             else:
#                 insertions += 1
#                 transcribed_index += 1

#         # Move the indices to the end of the match
#         original_index = match.a + match.size
#         transcribed_index = match.b + match.size

#     # Handle any remaining words
#     deletions += len(original_words) - original_index
#     insertions += len(transcribed_words) - transcribed_index

#     # Total words in original
#     total_words = len(original_words)

#     # Calculate WER
#     wer = (substitutions + deletions + insertions) / total_words
#     return wer

# # Original and transcribed text
# # original_text = """
# # Dan saya banggakan yang tidak sempat sebut namanya. Mohon maaf.
# # Sebelum saya.
# # Menyampaikan usul dan pertanyaan terlebih dahulu. Saya menyampaikan kepada kita semua bahwa.
# # Acara yang kita laksanakan pada hari ini saya apresiasi sangat apresiasi. Sudah lama saya dambakan ini.
# # Karena kami tidak tahu harus kadang mengadu ke mana.
# # Kadang kami menyurat tidak ditanggapi saya mau menyurat ke Mahkamah Agung.
# # Teman teman saya semua yang ada di sini.
# # Oleh karena itu pada kesempatan ini uh izinkan saya menyampaikan hal hal saran maupun mendapat maupun pertanyaan.
# # Barangkali kaitannya dengan uh proses pelayanan di Pengadilan negeri Makassar.
# # Ini berdasarkan pengalaman pak ya yang saya alami.
# # Karena saya spesialis penanganan perkara perdata.
# # Saya pernah dibuat stres juga.
# # """

# original_text = """
# Hidup adalah perjalanan panjang yang penuh dengan warna dan dinamika.
# Setiap langkah yang kita ambil membentuk cerita unik yang hanya kita yang bisa memahaminya secara utuh.
# Di setiap cerita, ada momen suka, duka, keberhasilan, dan kegagalan.
# Semua itu adalah bagian dari proses yang menjadikan kita manusia yang lebih kuat dan bijaksana.
# Bayangkan sebuah sungai yang mengalir deras, melintasi batu-batu, pohon-pohon, dan lembah yang curam.
# Seperti sungai itu, hidup kita akan selalu mengalir, meskipun kadang terasa terhambat oleh rintangan di sepanjang jalan.
# Namun, air sungai tidak berhenti.
# Ia mencari cara jalan lain, mengalir perlahan, dan akhirnya mencapai tujuannya, yaitu samudra yang luas.

# Begitu pula dengan kita.
# Dalam kehidupan ini, kita mungkin menghadapi hambatan yang tampaknya sulit diatasi.
# Tetapi, jika kita tetap tenang, sabar, dan percaya bahwa setiap masalah memiliki solusi, kita akan menemukan jalan keluar.
# Yang terpenting adalah bagaimana kita memandang masalah itu sendiri.
# Sebuah tantangan bukanlah akhir dari perjalanan, melainkan sebuah kesempatan untuk belajar sesuatu yang baru,
# untuk memahami kekuatan diri kita, dan untuk bertumbuh menjadi lebih baik.

# Dalam perjalanan hidup, kita juga perlu belajar untuk menghargai waktu.
# Waktu adalah sesuatu yang tidak dapat kita kendalikan atau kembalikan.
# Satu detik yang berlalu tidak akan pernah bisa diulang.
# Oleh karena itu, penting untuk memanfaatkan setiap momen dengan bijak.
# Jangan biarkan waktu terbuang sia-sia hanya karena kita terlalu sibuk dengan hal-hal yang kurang penting.
# Fokuslah pada apa yang benar-benar terjadi, pada hal-hal yang membawa kebahagiaan, manfaat, dan kedamaian dalam hidup kita.

# Selain itu, hubungan dengan orang lain adalah bagian penting dari kehi kebahagiaan hidup.
# Kita tidak hidup sendiri.
# Kehadiran keluarga, teman, dan orang-orang terkasih memberikan warna dalam kehidupan kita.
# Bersyukurlah atas kehadiran mereka.
# Jangan ragu untuk menunjukkan rasa terima kasih, memberikan dukungan, atau sekadar meluangkan waktu untuk mendengarkan mereka.
# Kadang-kadang, kebahagiaan sejati datang dari hal-hal kecil, seperti senyuman seorang teman,
# kata-kata penyemangat dari orang yang kita cintai, atau sekadar percakapan santai yang membuat hati tenang.

# Namun, jangan lupa bahwa mencintai diri sendiri juga adalah hal yang penting.
# Kadang, kita terlalu keras pada diri sendiri, mengkritik setiap kesalahan kecil yang kita buat.
# Padahal, kesalahan adalah bagian dari proses belajar. Tidak ada manusia yang sempurna, dan itu tidak apa-apa.
# Yang penting adalah kita selalu berusaha untuk menjadi lebih baik dari hari ke hari.
# Maafkan diri sendiri atas kesalahan di masa lalu dan fokus pada masa depan yang lebih cerah.
# Ingatlah bahwa setiap orang memiliki perjalanan masing-masing,
# dan tidak ada perjalanan yang lebih baik atau lebih buruk dari perjalanan orang lain.
# Semua perjalanan itu unik dan istimewa.

# Ketika kita mulai menghargai diri sendiri, kita akan lebih mudah melihat keindahan di sekitar.
# Keindahan itu bisa ditemukan di mana saja: dalam sinar matahari pagi yang hangat, dalam suara burung yang berkicau,
# atau dalam rasa puas setelah menyelesaikan tugas yang sulit.
# Hidup ini sebenarnya penuh dengan keajaiban kecil yang sering kali kita abaikan.
# Ambillah waktu sejenak setiap hari untuk merenung dan bersyukur atas hal-hal sederhana tersebut.

# Tidak hanya itu, ada satu hal lagi yang sering kali terlupakan: pentingnya menjaga kesehatan, baik fisik maupun mental.
# Tubuh kita adalah anugerah yang luar biasa, dan kita harus menjaganya dengan baik.
# Berolahraga secara teratur, makan makanan yang bergizi,
# dan cukup tidur adalah beberapa hal sederhana yang bisa kita lakukan untuk menjaga kesehatan fisik.
# Selain itu, kesehatan mental juga sama pentingnya. Jangan ragu untuk mencari bantuan ketika merasa stres atau tertekan.
# Berbicara dengan seseorang yang dapat dipercaya, membaca buku inspiratif,
# atau bahkan sekadar berjalan-jalan di alam dapat membantu menjaga kesehatan mental kita.

# Dalam kehidupan ini, kita juga perlu memiliki visi dan tujuan.
# Visi adalah pandangan jauh ke depan yang memberikan arah bagi hidup kita.
# Tanpa visi, kita seperti kapal tanpa kompas, berlayar tanpa tujuan yang jelas.
# Dengan memiliki tujuan, kita memiliki sesuatu untuk dikejar, sesuatu yang membuat kita bangun setiap pagi dengan semangat.
# Namun, ingatlah bahwa tujuan besar sering kali terdiri dari langkah-langkah kecil.
# Jangan terburu-buru ingin mencapai semuanya sekaligus. Nikmati prosesnya,
# dan rayakan setiap pencapaian kecil yang Anda dapatkan di di sepanjang jalan.

# Akhirnya, mari kita sadari bahwa hidup ini adalah anugerah.
# Tidak semua orang memiliki kesempatan yang sama seperti yang kita miliki sekarang.
# Jadi, mari kita manfaatkan hidup ini dengan sebaik-baiknya.
# Jangan hanya mengejar materi atau keberhasilan duniawi.
# Temukan makna sejati dalam memberi, berbagi, dan menciptakan dampak positif bagi orang lain.
# Ketika kita memberi tugas ketika kita memberi dengan tulus,
# kebahagiaan yang kita rasakan jauh lebih besar daripada apa yang bisa kita dapatkan dengan hanya menerima.

# Jadi, mari kita jalani hidup ini dengan semangat, harapan, dan rasa syukur.
# Setiap hari adalah kesempatan baru untuk menjadi versi terbaik dari diri kita sendiri.
# Ingatlah, hidup ini bukan hanya tentang mencapai tujuan, tetapi juga tentang menikmati perjalanan menuju ke sana.
# Setiap momen adalah bagian dari cerita indah yang kita tulis.
# Dan pada akhirnya, cerita itu akan menjadi warisan yang kita tinggalkan untuk dunia.
# """

# transcribed_text = """
# Perjalanan panjang yang penuh dengan warna dan dinamika.
# Setiap langkah yang kita ambil membentuk cerita unik yang hanya kita yang bisa memahaminya secara utuh.
# Di setiap cerita. Menu moment suka buka keberhasilan dan keahlian.
# Semua itu adalah bagian dari proses yang menjadikan kita manusia yang lebih kuat dan bijaksana.
# Bayangkan sebuah sungai buahnya deras melita sifat waktu pohon pohon dan membahayakan curang.
# Itu kita akan selalu mengalir meskipun kadang terasa terlambat oleh rintangan di sepanjang jalan.
# Air sungai tidak berhenti.
# Ia mencari cara jarang lain mengalir perlahan dan akhirnya mencapai tujuannya yaitu sumubra yang luas.

# Kita.
# Dalam kehidupan ini kita mungkin menghadapi hangatan yang tampaknya sulit diatasi.
# Tetapi jika kita tetap tenang, sabar dan percaya bahwa setiap masalah memiliki solusi, kita akan menemukan jalan keluar.
# Yang terpenting adalah bagaimana kita memandang masalah itu sendiri.
# Perjalanan melainkan sebuah kesempatan untuk belajar sesuatu yang baru,
# untuk memahami kekuatan diri kita dan untuk bertumbuh menjadi lebih baik.

# Kita juga perlu belajar untuk menghargai wanita.
# Waktu adalah sesuatu yang tidak dapat kita kendalikan atau kebalikan.
# Satu detik yang berlalu tidak akan pernah bisa diulang.
# Oleh karena itu, penting untuk memanfaatkan setiap momen dengan bijak.
# Jangan biarkan waktu terbuang sia-sia hanya karena kita terlalu sibuk dengan hal-hal yang kurang penting.
# Fokuslah pada apa yang benar-benar terjadi, pada hal-hal yang membawa kebahagiaan, manfaat, dan kedamaian dalam hidup kita.

# Selain itu, hubungan dengan orang lain adalah bagian penting dari kehi kebahagiaan hidup.
# Kita tidak hidup sendiri.
# Kehadiran keluarga, teman, dan orang-orang terkasih memberikan warna dalam kehidupan kita.
# Bersyukurlah atas kehadiran mereka.
# Jangan ragu untuk menunjukkan rasa terima kasih, memberikan dukungan, atau sekadar meluangkan waktu untuk mendengarkan mereka.
# Kadang-kadang, kebahagiaan sejati datang dari hal-hal kecil, seperti senyuman seorang teman,
# kata-kata penyemangat dari orang yang kita cintai, atau sekadar percakapan santai yang membuat hati tenang.

# Namun, jangan lupa bahwa mencintai diri sendiri juga adalah hal yang penting.
# Kadang, kita terlalu keras pada diri sendiri, mengkritik setiap kesalahan kecil yang kita buat.
# Padahal, kesalahan adalah bagian dari proses belajar. Tidak ada manusia yang sempurna, dan itu tidak apa-apa.
# Yang penting adalah kita selalu berusaha untuk menjadi lebih baik dari hari ke hari.
# Maafkan diri sendiri atas kesalahan di masa lalu dan fokus pada masa depan yang lebih cerah.
# Ingatlah bahwa setiap orang memiliki perjalanan masing-masing,
# dan tidak ada perjalanan yang lebih baik atau lebih buruk dari perjalanan orang lain.
# Semua perjalanan itu unik dan istimewa.

# Hari ini sendiri kita akan lebih mudah melihat keindahan di sekitar keindahan.
# Itu bisa ditemukan di mana saja dalam sinar matahari pagi yang aman dalam seorang burung yang berhijab,
# atau dalam rasa puasa telah menyelesaikan tugas yang sulit.
# Hidup ini sebenarnya pembentukan keajaiban kecil yang seringkali kita abaikan.
# Ambillah untuk sejenak setiap hari untuk merenung dan bersyukur atas orang hal yang sederhana tersebut.

# Terlupakan pentingnya menjaga kesehatan.
# Revisi momment kebangkitan adalah anugerah yang luar biasa dan kita harus menjaginya dengan baik.
# Berolahraga secara teratur, bahkan makanan yang bergizi,
# dan cukup tidur adalah beberapa hal sederhana yang kita lakukan untuk menjaga kesehatan fisik.
# Paling bisa mempunyai jangan ragu untuk mencari bantuan ketika merasa stres atau tertekan.
# Berbicara dengan seseorang yang dapat dipercaya membaca buku, inspiratif,
# atau bahkan sekedar berjalan jalan di alam dapat membantu menjaga kesehatan mental kita.

# Ini kita juga perlu memiliki visi dan tujuan.
# Visi adalah pandangan jauh ke depan yang memberikan arah bagi kehidupan kita.
# Kita seperti kapal tanpa kupas berlayar tanpa tujuan yang jelas.
# Dnggan memiliki tujuan. Kita memiliki sesuatu untuk dikejar sesuatu yang membuat Anda bangun setiap pagi dengan semangat.
# Namun ingatlah bahwa tujuan besar seringkali terhindari. Langkah langkah kecil.
# Jangan terburu buru ingin mencapai semuanya sekaligus nikmati prosesnya,
# dan meriahkan setiap pencapaian kecil yang anda dapatkan. Sedih sepanjang perjalanan.

# Akhirnya mari kita sadari bahidup ini adalah anugerah.
# Tidak semua orang memiliki kesem.
# Jadi mari kita manfaatkan hidup ini dengan sebaik baiknya.
# Jangan hanya mengejar materi atau keberhasilan dunia ini.
# Temukan makna senjata ini dan memberi bagi dan menciptakan dampak positif bagi orang lainnya.
# Ketika kita memberi tugas ketika kita memberi dengan tulus,
# kebahagiaan yang kita rasakan jauh lebih besar daripada apa yang bisa kita dapatkan dengan hanya menerima.

# Jadi mari kita jalani hidup ini dengan semangat harapan dan rasa syukur.
# Menjadi versus terbaik dari diri kita sendiri.
# Ingatkan hidup ini bukan hanya tentang mencapai tujuan, tetapi juga tentang menikmati perjalanan menunjuk kesana.
# Setiap momen adalah bagian dari cerita indah yang kita tulis.
# Dan perhatian cerita itu akan menjadi warisan yang kita tinggalkan untuk dunia.
# """

# # Calculate WER
# wer_value = calculate_wer(original_text, transcribed_text)
# print(f'WER in percentage: {wer_value*100}')


###############################################


import re
import os
from difflib import SequenceMatcher


def tokenize(text: str) -> list[str]:
    """
    Extract “word” tokens (alphanumeric + apostrophes) from text.
    Converts to lowercase so matching is case-insensitive.
    """
    # [\w']+ matches sequences of letters, digits, underscore, and apostrophe
    return re.findall(r"[\w']+", text.lower())


def calculate_wer(original: str, transcribed: str) -> float:
    """Returns WER as a fraction."""
    # orig_words = original.split()
    # trans_words = transcribed.split()

    orig_words = tokenize(original)
    trans_words = tokenize(transcribed)

    matcher = SequenceMatcher(None, orig_words, trans_words)
    matches = matcher.get_matching_blocks()

    subs = dels = ins = 0
    o_idx = t_idx = 0
    for m in matches:
        # handle the regions between matches
        while o_idx < m.a or t_idx < m.b:
            if o_idx < m.a and t_idx < m.b:
                subs += 1
                o_idx += 1
                t_idx += 1
            elif o_idx < m.a:
                dels += 1
                o_idx += 1
            else:
                ins += 1
                t_idx += 1
        # jump over the matched block
        o_idx = m.a + m.size
        t_idx = m.b + m.size

    # any trailing insertions/deletions
    dels += len(orig_words) - o_idx
    ins  += len(trans_words) - t_idx

    return (subs + dels + ins) / len(orig_words)


def batch_wer_by_levels(
    original_path: str,
    transcripts_dir: str,
    mic_type: str,
    levels=None
):
    # Read the reference once
    with open(original_path, 'r', encoding='utf-8') as f:
        original = f.read()

    # if user passed levels, prepare a set of strings for matching
    if levels is not None:
        level_set = {str(l) for l in levels}
    else:
        level_set = None  # means “auto-detect everything”

    # Pattern captures both xx (level) and yy (index)
    pat = re.compile(rf"Batch_parse_{mic_type}_60_(\d+)_(\d+)\.txt$")

    # Map level → list of WERs
    level2wers: dict[str, list[float]] = {}

    for fn in os.listdir(transcripts_dir):
        m = pat.match(fn)
        if not m:
            continue
        lvl, idx = m.group(1), m.group(2)
        # if user specified levels, skip others
        if level_set is not None and lvl not in level_set:
            continue

        path = os.path.join(transcripts_dir, fn)
        with open(path, 'r', encoding='utf-8') as g:
            transcript = g.read()

        wer_pct = calculate_wer(original, transcript) * 100
        level2wers.setdefault(lvl, []).append(wer_pct)

    # Print out results
    for lvl in sorted(level2wers, key=lambda x: int(x)):
        wers = level2wers[lvl]
        avg  = sum(wers) / len(wers)
        print(f"Noise {lvl:>3}%: {len(wers):>3d} files → avg WER: {avg:6.2f}%")


if __name__ == '__main__':
    MIC_TYPE = 'tws'
    TXT_FILE_PATH = f'data_log/audacity/new_self-talk/{MIC_TYPE}/batch_parsed'
    LEVEL = 100
    batch_wer_by_levels('original.txt', TXT_FILE_PATH, MIC_TYPE, levels=[LEVEL])
