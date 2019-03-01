�
fy\c           @   sm   d  Z  d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d d �  �  YZ	 d S(   s   
Class for AI bot
i����N(   t   time(   t   deepcopyt   Player8c           B   sz   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z d �  Z d �  Z RS(   s    
    AI implemented 
    c         C   sX  d |  _  d |  _ d |  _ d |  _ d |  _ d |  _ d |  _ d |  _ d |  _ d d g |  _	 g  |  _
 d d d g d d d g d d d g g d d d g d d d g d d d g g g |  _ d d g |  _ d |  _ d |  _ i  |  _ d d d d d d d d d d d d d d d d d d g |  _ x( t d � D] } |  j
 j d	 | � q6Wd
 S(   s&   
        Initialize variables
        i    i   i	   I �T   i   t   ot   xi$   i   N(   i    i    i    iQ   i�  (   i    i    i    (   t   defaultt   limitt   startt   maxdeptht   playert   opponentt   bestmvt   inft
   max_playert
   map_symbolt	   zob_storet
   hash_storet   bonus_move_curt   last_blk_wont   numstepst   dictt   blockweightt   ranget   append(   t   selft   i(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   __init__   s&    										W			?c   	      C   sU  xNt  d � D]@} x� t  d � D]� } g  } | j | j | | d � | j | j | | d � | j | j | | d � |  j | | � } |  j | d | d c | 7<|  j | d | d d c | 7<|  j | d | d d c | 7<q  Wx� t  d � D]� } g  } | j | j | d | � | j | j | d | � | j | j | d | � |  j | | � } |  j | d | c | 7<|  j | d | d c | 7<|  j | d | d c | 7<qWg  } | j | j | d d � | j | j | d d � | j | j | d d � |  j | | � } |  j | d c | 7<|  j | d d c | 7<|  j | d d c | 7<g  } | j | j | d d � | j | j | d d � | j | j | d d � |  j | | � } |  j | d d c | 7<|  j | d d c | 7<|  j | d d c | 7<q Wd	 S(
   s+   
        Find weights of each cell
        i   i   i    i   i	   i   i   i   N(   R   R   t   small_boards_statust   calculatewincombsbR   (	   R   t   boardt   symbolt   bR   t   rowt   tempt   colt   dig(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   smallboardutility,   sF    #'#c         C   s_  d } | d k r d } n d } | j  | � d k rX | j  d � d k rX | d 7} n{ | j  | � d k rz | d	 7} nY | j  | � d k r� | j  d � d k r� | d
 7} n" | j  | � d k r� | d 7} n  d | k r� | d 7} no | | k r| | k r| d 7} nJ | | k r6| | k r6| d 7} n% | | k r[| | k r[| d 7} n  | S(   s;   
        Calculate weight from each row,column,dig
        i    R   R   i   t   -i   id   i   i�  ij���i$���t   dg      �i   i����(   t   count(   R   t   vR   t   weightt   opp(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyR   h   s*    	**c         C   s	  |  j  | } d } | d k r( d } n d } | j | � d k r� | j d � d k r� | d 7} | d k  r{ | d	 7} q:| d
 7} n� | j | � d k r� | d 7} | d 7} n� | j | � d k r| j d � d k r| d 8} | d k  r| d 7} q:| d 7} n, | j | � d k r:| d 8} | d 7} n  | | k ri| | k ri| d 7} | d 7} n� | | k r�| | k r�| d 7} | d 8} n` d | k r�| | k r�| | k r�| d 7} n/ | | k r�| | k r�| d 7} | d 8} n  | |  j  | <| S(   s9   
        Calculate status of each row,column,dig
        i�   R   R   i   R%   i   i
   i    i'  i(#  i   id   i�� i���i ���i���g      �?g�������g333333�?g333333�?(   R   R'   (   R   R(   R   t   blknot   blkwtt   utilityR*   (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   calculatewincomb�   sD    	*

*



$
c         C   s�  g  } d | d | | d } x� t  d � D]� } g  }	 |	 j | j | | | | � |	 j | j | | | | d � |	 j | j | | | | d � |  j |	 | | � }
 | j |
 � q- Wx� t  d � D]� } g  } | j | j | | | | � | j | j | | d | | � | j | j | | d | | � |  j | | | � }
 | j |
 � q� Wg  } | j | j | | | � | j | j | | d | d � | j | j | | d | d � |  j | | | � }
 | j |
 � g  } | j | j | | | d � | j | j | | d | d � | j | j | | d | � |  j | | | � }
 | j |
 � t | � S(   s=   
        Calculate utility of each cell of big board
        i	   i   i   i   (   R   R   t   big_boards_statusR.   t   sum(   R   R   R   t   rt   cR   t   utilityvectorR+   R   R    R!   R"   R#   (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   blockutility�   s:     $$ $$$$ $ c   	      C   s�   d } d d d d d d d d d d d d d d d d d d g |  _  |  j | | � x� t d � D]� } xy t d � D]k } xb t d � D]T } |  j | | d | | d | � } |  j  d | | d | } | | | 7} q� Wqu Wqb W| S(   s$   
        Heuristic function
        i    i   i   i   i	   (   R   R$   R   R4   (	   R   R   R   R-   R   t   jt   kt   aR   (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyR-   �   s    ?#c   
   	   C   sI  i  |  _  x9t d � D]+} x"t d � D]} xt d � D]� } d } | d k r] d } n d } x� t d � D]� } x� t d � D]� } | j | d | | d | | }	 |	 |  j |  j k r� | |  j d | N} n6 |	 |  j |  j d Ak r| |  j d | d N} n  | d 7} q� Wqp W| |  j | | | <q< Wq) Wq Wd  S(   Ni   i   i    i   i   (   R   R   R/   R   R   R   R   (
   R   R   t   mR   R5   t
   hash_valuet   hash_variableR6   t   lR   (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   initialise_hashtable  s"    		%c         C   s�   | d } | d d } | d d } | d k rS d | d d | d d } n" d | d d | d d d } | |  j  k r� |  j | | | c |  j d | N<n* |  j | | | c |  j d | d N<d  S(   Ni    i   i   i   i   (   R   R   R   (   R   t   moveR	   t	   board_numt   row_numt   col_numt   hash_var(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   update_hashtable6  s    
!")c         C   s�  t  �  |  j |  j k r3 |  j | |  j |  j � S| j �  d k sQ | d k rk |  j | |  j |  j � S| j | � } | |  j k r� |  j	 }	 n	 |  j	 }	 |  j
 | }
 x?| D]7} |
 |  j
 | <|  j | | � | j | | |  j | � \ } } | r|  j
 | c d N<n d |  j
 | <| |  j k r�| r�|  j
 | d k r�t |	 |  j | | d | | | | | � � }	 d |  j
 | <n2 t |	 |  j | | d | d A| | | | � � }	 t | |	 � } n� | r"|  j
 | d k r"t |	 |  j | | d | | | | | � � }	 d |  j
 | <n2 t |	 |  j | | d | d A| | | | � � }	 t | |	 � } |  j | | � d | j | d | d | d <d | j | d | d d | d d <| | k r�Pn  t  �  |  j |  j k r� Pq� q� W|
 |  j
 | <|	 S(   s#   
        minimax+alphabeta
        t   CONTINUER%   i    i   i   i   (   RC   R%   (   R    R   R   R-   R   R	   t   find_terminal_statet   find_valid_move_cellsR   R   R   RB   t   updatet   maxt   prunealphabetat   minR/   R   (   R   R   t   depthR	   t   player_movet   alphat   betat   prevt   moves_availablet   cur_utilityt   tempbonusmovet   movest   gamepost   status(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyRH   G  sP    	"!)c      	   C   s�  | j  | � |  _ |  j } |  j | } xu|  j D]j} | |  j | <|  j | | � | j | | |  j | � \ } }	 |	 r� |  j | c d N<n d |  j | <|	 r� |  j | d k r� |  j | | d | | |  j |  j | � }
 n0 |  j | | d | d A| |  j |  j | � }
 d | j | d | d | d <d | j	 | d | d d | d d <|  j | | � |
 | k r3 | |  j
 k r3 | } |
 } q3 q3 W| |  j | <| S(   s8   
        Preprocessing for alpha beta algorithm
        i   i    R%   i   i   (   RE   t	   nextmovesR   R   RB   RF   R   RH   R/   R   R   (   R   R   t   old_moveR	   RJ   t   curmaxRQ   RR   RS   RT   t   player_utilityt   cur_best_move(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   alphabetamove�  s*    
"/0!)	c         C   sV   xO t  d |  j � D]; } t �  |  j |  j k r6 Pn  |  j | | | | � } q W| S(   s(   
        idfs returns best move
        i   (   R   R   R    R   R   RZ   (   R   R   t   oldmvt
   tree_levelR	   RJ   t   output(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   idfs�  s
    c   
      C   s�  t  �  |  _ | d k r6 d |  _ d |  _ d |  _ n d |  _ d |  _ d |  _ y(| d k rg |  j Sd } t | � } d d g |  _ |  j r� |  j |  j c d N<n d |  j |  j <|  j	 | | | |  j � } | j
 | | |  j |  j � \ } } | r|  j d N_ n	 d |  _ d | j | d | d | d <d | j | d | d d | d d <t  �  |  j GH| SWn6 t k
 r�}	 d G|	 GHd	 Gt j �  GHt j �  GHn Xd
 S(   s   
        Main code
        R   i   i    i����R%   i   i   s   Exception occurred s   Traceback printing N(   i����i����i����(   R    R   R   R	   R
   R   R   R   R   R^   RF   R   R/   R   t	   Exceptiont   syst   exc_infot	   tracebackt
   format_exc(
   R   t	   gameboardt   oldmoveR   RJ   t	   tempboardt   tempmoveRT   t   blk_wont   e(    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyR=   �  s<    						%	!)	(   t   __name__t
   __module__t   __doc__R   R$   R   R.   R4   R-   R<   RB   RH   RZ   R^   R=   (    (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyR      s   		<	$	7	:	"			L	C	(    (
   Rl   t   randomRb   R`   t   numpyt   npR    t   copyR   R   (    (    (    sI   /home/nsk06/Documents/artificial intelligence/latest work/latest/team8.pyt   <module>   s   