
import time
class bcolors:
    GREEN = '\033[92m'
    ENDCOLOR = '\033[0m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    MAGENTA = '\033[35m'
    BLUE = '\033[34m'

import sys

import random

count = 0



### Spacer
def spacer(input):
    time.sleep(input)
    print(" ")


# Game over screen

def gameover():
    print(""" 
 ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .       ▌ ▐·▄▄▄ .▄▄▄   ▄▄ 
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀· ▄█▀▄ ▪█·█▌▀▄.▀·▀▄ █· ██▌
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄▐█▌.▐▌▐█▐█•▐▀▀▪▄▐▀▀▄  ▐█·
▐█▄▪▐█▐█▪ ▐▌██ ██▌▐█▌▐█▄▄▌▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌ .▀ 
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀  ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀  ▀ 
""")
    
# you win screen
def youwin ():
    print("""
 ▄· ▄▌          ▄• ▄▌    ▄▄▌ ▐ ▄▌  ▪     ▐ ▄    ▄▄ 
▐█▪██▌   ▄█▀▄   █▪██▌    ██· █▌▐█  ██   •█▌▐█   ██▌
▐█▌▐█▪  ▐█▌.▐▌  █▌▐█▌    ██▪▐█▐▐▌  ▐█·  ▐█▐▐▌   ▐█·
 ▐█▀·.  ▐█▌.▐▌  ▐█▄█▌    ▐█▌██▐█▌  ▐█▌  ██▐█▌   .▀ 
  ▀ •    ▀█▄▀▪   ▀▀▀      ▀▀▀▀ ▀▪  ▀▀▀  ▀▀ █▪    ▀ 
""")
    

# boss apple
def boss_apple():
    print("""
                                                                           .o,                                                          
                                                                        .:oldx;         .xNl                                                          
                                                                    .. .dxldOd.         :KKc                                                          
                                                                 .cllxOKx:xNd.         .xxkl      .:'                                                 
                                                               'loodoo0O;dd,.          ck,ox.     :Nl                                                 
                                                             .ldcldc.;k;cO'           .xo :k,     lWl     .;;.                                        
                                                            .ko.:O,  ok.dk.           :k' .xo     lWl    :xk0;                                        
                                                           ,xl. lx.  lkc0O'           dd.  ;O:    :Xc   ,Occk'                                        
                                                         ,dXk.  lx.  cOd0K,          .kc    lk.   ;O;   ck;do          ;o;                            
                                                       ,o0Ko.   lx.  ;K0OXc          ;O;    ;k,   cK;   oxox'        'okXl                            
                                       .o:           .cOKk;     lx.  .OKkXk:.        ck'    ;k,   dK,  .k0k:        'xlxx.                            
                                      .Ok.          .lKKo.      lx.   oXOk0Xl        ox.    ;k,  'O0'  ;0Kx.       ,xc.kl                             
                                     .xNo           :KK:        lx.   ,0Kdx0k,      .xl     ;k,  lNd   lOkx.      ;k: .xd                             
                                     dkdO,        .l0Kd.        lx.   .kXd,.dd      :O,     ;O, .xX:   lxdx.     ,Oc   lx.                            
                                    ,00d0d       .dxlkx'        lx.    oNx. :O'    .xo      ck. :XO'   lxdx.     ox.   :O,                            
                                    dXOlck:      .kl.oOc.       lx.    lNx. .kl    ck'      dd .OWo    oxxx.    'k:    'Oc                            
                                   '0Kk: :k;     .xo ;kx'       ck'    dNd.  lx.  ,k:      .kl.oXXc   .xxko     lx.    cXd                            
                                   ;KKd'  ;x:     :kcckx'       ;O;   .xNl   ;O; .xo       .xkddoO;   lkdk,    'kc     lNd.   .:l:.                   
                                   :K0c.   ,k:    .OXxl.        .xl   ;KK:   .kl.od.       ,KNd.,k; .lx;dd.    ox.     oNx.  ;dd0o                    
                                  .xXd.     :k;  .cKX:           cO'  oXO;    c0kl.        cXd. ,Odcoc..xl    .kl      lNk. ck,.xl                    
                               'c':K0,       :k: .dK0,           'Oc ,0Kx'    ,kc          .'   .lo;.  .xl    lx.      lNx.;k; .xl                    
                            .;ooOOONd.        'xo'l0X:            od.dXOl.     .                       .do   ck;       lXx.ox. .xl                    
                           ;kKd.cXXXc          .ldokO'            l0x00k:  ...                          ck,'oo'        lNd:kc   ox.                   
                         .dKOd;.;KWK,            ;KO'             c0old:.'lcod,                         'xxo;          lXdok,   lk.                   
                        .xKOl.  .xWO.            .c;              ..     .okocl.                         ..            lXxkk.  .x0'                   
                        lXO:.    cNO.                                     .;l:c;                                       lXk0d.  .xNd.                  
                       .OXl      ;XNo.                        ......    .';:dl:dc;'.                                  .xX0Kc    ;KK;                  
                       '0K,       oNNk;.                .:llloxOO000Oxox0KKKKxodld00xl::ccoddxddol:'.                 'OXOc      lXk. ..              
                       '0K,       .dXNKd.            .;oOOdooxO0KKKKKXXXKKKKX0dolxKKXXXXXXXXKKKKOdxkdo;                ...       ,0K,.xl              
                       .OXc        .x00Xd.         ,d0XK00KKKKKKKXNNNNNNXXKKXKxx0KXKXNNXKKKKKKKKKK0OOOOx:.                       ,0K;:Kc              
                   .    oNO'        .d0KXl       'dXXKKXXKKKKKKKKXXXXXXXNNNNNKxdxKNNWNXXKKKKK00KKKKKKK0OOk:                      :X0dK0'              
                  ,d,   .xXx,        .dOxkc.   .c0XKKXNNXKKKKKKKKKKKKKKKKXXXX0kxx0KXXKKKKKKkc'.,;,';d0KKOkkd.                   .ONNO0x.              
                  ;0:    .dKO:         :dOXd. 'kXXKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:        .oKKK0kOO,                 .dNWXdkl               
                  ,Kd.    .kXx;          ,dKOlkNKKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx,        .xKKKK0K0;               'xNWXlck,               
                  ;KKc     ;0Kk:.          .cOOkKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:        ;0KKKKKX0,             ,0NNXk;dd.               
                  ;Odxo.    'kKO;           okcxKKKXNNXKKKKKKKKKKXXXKKKKKKKKKKKKKKKKKKKKKKKKKk'        ;kKKKKKXk.           .ONKK0c'xl                
                  ;O:.do.    .xNx'         ,kodKKKXNNXKKKKKKKKKKKXNNXKKKKKKKKK0KKKKKKKKKKKKKKKl         :0KKKKKXo           .,,ckk,.xl                
                  .kkc:lx;    .kXx.        c0k0KKKXNNKKKKKKKKKKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKx.        .dKKXNKKk'            .cOo..xc                
                   oXOk:,xo.   .kXx.      .xkxKKKXNNXKKKKKKKKKKKKXNNKKKKKKKKKKKKKKKKKKKKKKKKKKk.         cKKXNX00:            ,xk: ,k:                
                   :0kxx;.dx.   '0Xl.     :klxXKKXNXKKKKKKKKKKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKKx.        .dKKXNKk0c            cOd. ;kl:.              
                   .dOlxx;.:dl.  cX0c.   .dx:OKKKXNXKKKKKKKKKKKKXNNXKKKKKKKKKKKKKKKKKKKKKKKKKKd.        :0KKXWkl0c           .dk:  lOkO,              
                    .dxoxx; .:ol;;OKk:   .Od:0KKKXNXKKKKKKKKKKKXNNXKKKKKKKKKKKXKKKKKKKKKKKKKKX0:       .dKKKXNxoO;          .oko. ,OKNx.              
                     .okoxk:.  'cxXN0d'  'Oc;0KKKXNXKKKKXXXKKKKXNNXKKKKKKKKKKXNXKKKKKKKKKKKKKXNKd:.   .l0KKKXNkxk.         .cOd. .kXXNl               
                      .ckOOkl.   .cKXOc. .ko;OKKKXNXKKKXNNXKKKKXNNXKKKKKKKKKKXNXKKKKKKKKKKKKKXNNXKOdllx0KKKKXXO0o          :kx,.;x0KKO,               
             .cl.       'xKOkd'    oX0c.  cklxKKKXNNXKKXNXKKKKKXNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKKKKXXX0,         'xkc;ddoOdko                
             .dNx.       .cO0Od,   .,,.   .xkdKKKKXNXKXNNXKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKKKKXKXd.        'okOOd;,ko'xl                
              'ONk:.       'xK0kl.         ;0OOKKKXNNXXNXKKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKKKK0X0,        .o0KO:.cxc.'kc                
               'kOdd:.      .:0Kkx:.       .dXKKKKKXNNNNXKKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKKKxkNx.        .xk:,cxl.  :O,                
                .lx0KOo'      'xKOkl.       ,KNKKKKKNWWNKKKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKKk:xNl        'OKxllc.    ox.                
                  'd0KKOdc'    .c0Kk;        lXXKKKKXWWNXKKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKK0llK0c        .;:,.      ,k:                 
                    ,xKKOkkolccclxx,         .xNKKKXNNNNXKKKKKXNNXKKKKKKKKKKXNNXKKKKKKKKKKKKKXNNXKKKKKKKKdl00kl                  .ko                  
                      'lO00kxxxxo;..          ,KNKKXNNNWWNNXXKKXNXKKKKKKKKKKKNNXKKKKKKKKKKKKKXNNXKKKKKKKOxOdoOc                  lk.                  
                       ;doldxkO000Okdc:,.      lNNXXNWNNWWWNNNXNNXKKKKKKKKKKKXNNXKKKKKKKKKKKKXNXKKKKKKKKxOk'cOc                 ,kc                   
                      :kxx;   ..,::lkK0kc.     .oXNNWWNNNWWWNNNNNXKKKKKKKKKKKXNNXKKKKKKKKKKKKXNXKKKKKKKkkO;.cOc             ,occxc                    
                     .do :k,        .cOo.       .oNWWNNNNNWWWNNNWNXXXXXKKKKKKXNNXKKKKKKKKKKKXNNXKKKKKKkkO; .dO:           .lkxxOc                     
                     .kd..ck,         ,kc        .oNWNNNNNNWWWNNWWNNNNNNXXKKKKXNXKKKKKKKKKKKXNNXKKKKK00k;  :kd.          ;xkolOo                      
                      lKOo;lk,         'xc        '0WNNNNNNNWWWNWWNNNNNNNNXXXXNNNXKKKKKKKKKKXNXKKKKKKXx.  .oOc        .,okd;:kl.                      
                      .lK0kloxl'        'kl.      .dNWWWNNNNNWWWWWNNNNNNNNNNNNNWWXKKKKKKKKKKNNXKKK00Kd.   ,kx,       ,dkd;.ck:                        
                        ;x00kdddll:.     'xo.      c0KWWWNNNNNWWWWNNNNNNNNNNNNNWWNNNNNXKKKKXNNKKKKKOc.   'dkl.     .:kkc..lx'                         
                          'ck00d::col:.   .dd.     ckk0NWWNNNNNWWWNNNNNNNNNNNNNWWNNNNNNNXKKXNXKKXXO,    'dkl.     .lkd;.:dl.                          
                             ,oOKOo:loolc:;:xko;'. ,xkkO0XNWNNNWWWWWNNNNNNNNNNWWWNNNNNNNNKXNNXXXO:.    'dkl.    .cxxooooc.                            
                               .;ok000kxkOOkkO0OkdodOOkOd;:dkKNWWWWWWWNNNNNWWWWWNNNNWWWWNXNWNKkc.    .;dkl.   'cxxxddo,                               
                                   .,codxkO00Ol,...;okkkd.   'cddolooool;':ox0K00Okdclddox0Kx,    ':oxxo,..;coxxkOko'                                 
                                          .',:llol,.,xkOd.         .:l:'..   .'clccccll:,ckx, .;coO0OkxocoOK00Okdc.                                   
                                                .,clok00x.        .xd;:llooolcxOkkdxOd::oxkxlcd0K000KK0kkxdcc;,.                                      
                                                    .':llll:,..':lo:.    .',,;,.             ..,:cc:,,..                                              
                                                          .:llclc'                                                                       """)
    # southpark shoe gift art
def southpark_shoe():
     print("""                                                                                                               
                                                                                  .;cloolllloo;.                    .;cok000OOOOOOOOkO0KKX0c.         
                                                                                ,oxxdollccllldxxdl:'.        .;coddxOKKOOOOOOOOO000000O0K0xxx,        
                                                         ..',,'.              ,dkocccccccccccccccoxxdoc..,cld0XK0OOOOOOOO000KKKKKXXKXNKOdcccOO'       
                                                    .,cdO0XWWWNKOkxdl;,.   .,dOxc:ccccccccccccccccc:clxkOK000OOOO0000KKKKKKKKKKKKKK0Oxoccco0NNo       
                                                  ;xKNMMWKOxddxkOKWMWWWX0kk00OkkkkxlccccccccccccccccccccxK0O00KKKKXKKXKKKKKKKKKKKK0xccccdONXxkk.      
                                                .xNMMXkc,.     .:k00XWMMMMMMWNWMMMWXd:ccccccccccccccccccxXKKKXKKKKKKKKKKKKKKKKKXKOocccckNXkl:o0:      
                                                dWMNd'    .,codONWNNMMMMMMMMMMMMMMMMKkxddlcc:::ccccccc:lOK0KKKKKKKKKKKKKKKK000OkocccclON0occ:cOo      
                                               .xMMXd:clokKWMMWNXNXXKXWMMMMMMMMMMMMMMMWWWXX0OOkdl:ccccckXKKKKKKKKKKKKKKKXXK0kdc:cccc:dNKl:cccckd.     
                                              .,xNMMMMMMWWMMMMNK0OkxdxOXWMMMMMMMMMMMMMMMWNNWMMMWXOxoloONMNNXKKKKKKKKXXK0kxdlccccccc:oKNdccccc:dk'     
                                         .;dkOO0kkXMMMWKkkKWMMMMMWWX00kkO0NMMMMMWWWMMMMMNOkkOKXNWMMNXNWkxXWXKXKKKK0Okxoc::cccccccc:cONkcccccccoOo     
                                    .'coodxdx0XX0O0NWMMWXOkOXMMMMWNWMMWNNKKKNMMMWXKKXNWMMWXK0OxxOXWMWMWKdxXX0OkxdolccccccccccccccccxN0l:ccccccck0,    
                               .;llodxdocc:cccox0XXX00KNWWNXKKNMMNKO0KXNWMMMMMMMMMWKOkONMMMMMXO0XNKkx0WMWK0N0c::ccccccccccccccccc:l0Nx:ccc:cldxOO,    
                          .,:lodxdocccccccccccccclxOKX0Ok0NMWNNMMMMNOxxxO0KXXNWMMMMMWXOONMMWXNNXOdlc:lkNMMWWWOlcccccccccccccccccc:oX0l:ccldxkkdO0;    
                       .;ldkdoc::cccccc:ccccccccccc:lxO0K0KXNWMMMMMMWKkdxxxxxkO00XNWWMXk0WMMW0dlcccccccdXMMMMW0lccccccccccccccccccxNOlodxxkxxxdOKc    
                    'cdxxoc:cccccccccccccccccccccccccc:cok0KXNWWWMMMMMN0kxxxxxxxddxOXWWXKNMMWOcccccccccco0WMMMW0l:cccccccccccccccckWKxkkxxxxxxdxKO.   
                 .:dxxocccccccccccccccccccccccccccccccccc:clx0NWNXXNMMMWN0xdxxdx0KKXX0kdlo0WMW0occcccccc:lOWMMMNxccccccccclloodddxKW0xxxxxxxxxx0WWx.  
               'lxkoccccccccccccccccccccccccccccccccccccccccccoxOXXXNNNMMW0xk0KXX0xdlc:cc:lOWMMNOoccccccc:lONMMM0c:cllloddxkkkkkxxXNOxxxxxxxxx0NMMWl  
             'dkdlccccccccccccccccccccccccccccccccccccccccccccc:coxOXXXWMMNXK0Oxoc:cccccccccd0WMMN0xoccccc:l0MMWNOxdxkxxxxxxxxxxxkXNOxxxxxk00XWMMMMK, 
           .lkdccccccccccccccccccccccccccccccccccccccccccccccccccccclx0XWNOdlccc:ccccccccccc:cdOXWMMNOocccll0WMNXWKxxxxxxxxxxxxxdkXNOxxkOKNMMMMMMMMX: 
          ,kklccccccccccccccccccccccccccccccccccccccccccccccccccccccccclx0NX0xl:cccccccccccc:ccclx0WMMN0kkO0NMMXOKNOxxxxxxxxxxxxdONNKXXNWMMMMMMMMMWx. 
        .lOxccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccclxk0XKOdlccccccccccccccc:lkXWMMWWWWMMW0dxXXkxxxxxddxkO0KNWMMMMMMMMMMMMMMM0,  
       .x0l:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:cox0XXOocccccccccccclodkkO0KKKKKK0OxxONNOddxxO0KXWWMMMMMMMMMMMMMMMMMWNl   
      ;kOxl:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:coOXXkocccccclodxkkxxxxxxxxxxxdxxONN0O0KXNWMMMMMMMMMMMMMMMMMMMN0xc'    
     ,kOdkxc:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccokXN0xlcodxkxxxxxxxxxxxxxxkOKNWMWNWMMMMMMMMMMMMMMMMMMMMW0xc,.       
     c0xdxkdlccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccclxKNKKK0kxxxxxdxxxxxxkOXNWMMMMMMMMMMMMMMMMMMMMMMMWKkl;.           
    .x0xxxxkkdcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccldxkkkOKXXXXK00K000KXXNWMMMMMMMMMMMMMMMMMMMMMMWKxl;.               
    '0NOxxxxxkxdlccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccodxkxxxxxxxkOOO0KKXNWMMMMMMMMMMMMMMMMMMMMMMMWKko;.                   
    ,KMNKOxxxxxkkdooccccccccccccccccccccccccccccccccccccccccccccccccccccccc:c:coxkxxxxxxxxxxxxxxkOKNWMMMMMMMMMMMMMMMMMMMMWXOo;.                       
    ,KMMMWXOxddxxxkkxdooolccccccccccccccccccccccccccccccccccccccccccccccclooodxkxxxxxxxxxxxxxxkKNWMMMMMMMMMMMMMMMMMMMMNOo:.                           
    ;XMMMMMMNXK0OkxxxxxkkxxddddooolllcccccccccccccccccllloooooddddddddddxkkkxxxxxxxxxxxxxxkO0KNMMMMMMMMMMMMMMMMMMWN0dc'                               
    cWMMMMMMMMMMMNXKOOOxddxxxkkxkkxxxxxxxxkxxxkkxxkxxxxkkkkkkkkkkkkkkkkxxxxxxxxxxxxkk00KXNWMMMMMMMMMMMMMMMMMMWN0d:'.                                  
    ,KMMMMMMMMMMMMMMMMWNK0OOkkkxxddxxxxxdxxxxxxxxxxxxxxxxxxxxxxxxdxxxxxkOOO00000KXNNWMMMMMMMMMMMMMMMMMMMMMW0d:'.                                      
     lXMMMMMMMMMMMMMMMMMMMMMWNNXK0O0OkkxxxxxxxxxxxxxxxxxxxkO0O0KKKKXXNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0dc,.                                          
      ,xXMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNXXKKKKKKKKKKKXNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdc,.                                              
        .lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl;.                                                  
          .xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOo;.                                                      
            ,oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0kxol,.                                                          
              .:d0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0Okdlc:,'..                                                                
                 .'ckKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNKOxxoc:;'...                                                                          
                     .':cox0NWMMMMMMMMMMMMMMMMMMMMMWWNX0Oxdl:,,'.                                                                                     
                           .';coxKXKXNNNWWWNX0Oxolc;,...                                                                                              
                                 ....''',,,'..                                                                                                        
                                                                                                                                                      """)

# Boss dodge game fucntions

def boss_dodge():
    print("You successfully dodge the apple.")
    spacer(1)
    boss_apple()
    spacer(1)

def boss_dodge_fail1():
    print("You get hit by the apple and knocked to the floor, you get back up.")
    spacer(1)

def boss_no_choice():
    boss_choice()
    spacer(1)

def boss_choice():
    boss_choice = input (f"{bcolors.GREEN}⚡THE SOLE SENTRY OF THE APPLE EMPIRE⚡{bcolors.ENDCOLOR} charges up and fires an apple at {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Do you dodge? 'left' or 'right' ")
    spacer(1)
    boss_apple()
    spacer(1)

    if boss_choice == "right":
        boss_dodge()
        spacer(1)
    elif boss_choice == "left":
        boss_dodge_fail1()
        spacer(1)

    else:
        boss_no_choice()
        spacer(1)  

# second phase of end boss
def boss_dodge2():
    print("You successfully dodge the second attack, just barely! You see that the contraption is starting to get more worked up!")
    spacer(1)

def boss_dodge_fail2():
    print("You get hit by the contraptions second attack, you fall to the ground and everything fades to black... Gameover!")
    spacer(1)

def boss_no_choice2():
    boss_choice2()
    spacer(1)

def boss_choice2():
    boss_choice2 = input (f"> {bcolors.GREEN}⚡THE SOLE SENTRY OF THE APPLE EMPIRE⚡{bcolors.ENDCOLOR} winds up another attack and fires a second apple at {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Do you dodge this attack? 'left' or 'right' ")
    spacer(1)
    if boss_choice2 == "right":
        boss_dodge2()
        spacer(1)
    elif boss_choice2 == "left":
        boss_dodge_fail2()
        gameover()
        sys.exit()
    else:
        boss_no_choice2()
        spacer(1)

# final phase of boss fight
def boss_dodge3():
    print ("You suceesfully dodge and counter attack by deflecting the apple back at the contraption... the apple fires back into the dispenser and the contraption explodes!")
    spacer(1)

def boss_dodge_fail3():
    print ("You get hit by the contraptions final attack, it stuns you but you see an opportunity to throw the apple back at the contraption... It hits! The apple you threw goes back into the contraption and causes a blockage leading to the contraption over heating and exploding! You get caught in the blast and everything fades to black...")
    spacer(1)

def boss_no_choice3():
    boss_choice3()

def boss_choice3():
    boss_choice3 = input (f"{bcolors.GREEN}⚡THE SOLE SENTRY OF THE APPLE EMPIRE⚡{bcolors.ENDCOLOR} is riled up and sends a final blow... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Do you dodge this final attack? 'left' or 'right' ")
    spacer(1)

    if boss_choice3 == "left":
        boss_dodge3()
        youwin()
        sys.exit()
    elif boss_choice3 == "right":
        boss_dodge_fail3()
        gameover()
        sys.exit()
    else:
        boss_no_choice3()

# chinpokemone choice fucntion 

def stegmata():
    print(f"{bcolors.MAGENTA}You cant have that one! Stegmata is mine, he's so kewl you guys!{bcolors.ENDCOLOR}")
    spacer(1)
def pengin():
    print(f"{bcolors.MAGENTA}Sorry new kid, this ones Kenny's! I promised id get him a Pengin of his own. He's off playing princess right now so I can't give it to him yet.{bcolors.ENDCOLOR}")
    spacer(1)
def ferasnarf():
    print(f"{bcolors.MAGENTA}Oh man, that's Stan's Ferasnarf, he's gonna use it to impress Wendy and steal her from Token!{bcolors.ENDCOLOR}")
    spacer(1)

def pick():
    chinpokemon_choice()

def chinpokemon_choice():
    chinpokemon_choice = input (f"{bcolors.BLUE}Here pick one for yourself! Which one do you want?{bcolors.ENDCOLOR} 'stegmata', 'pengin' or 'ferasnarf' ")
    spacer(1)
    if chinpokemon_choice == "stegmata":
        stegmata()
        spacer(1)
    elif chinpokemon_choice == "pengin":
        pengin()
        spacer(1)
    elif chinpokemon_choice == "ferasnarf":
        ferasnarf()
        spacer(1)
    else:

        pick()
        spacer(1)

# Shoe choice

def shoe_yes():
    print(f"{bcolors.BLUE}Awesome dude! I was gonna give this to Cartman for his birthday but as you see hes always being mean!{bcolors.ENDCOLOR}")
    spacer(1)
    
def shoe_no():
    spacer(1)
    print(f"{bcolors.BLUE}Take it anyways dude, I dont want Cartman to have it. He's always acting like this. You deserve it more!{bcolors.ENDCOLOR}")

def shoe_wrong():
    shoe_choice()

def shoe_choice():
    shoe_choice = input (f"{bcolors.BLUE}Hey dude are you gonna take it or not?{bcolors.ENDCOLOR} 'yes' or 'no' " )
    spacer(1)
    
    if shoe_choice == "yes":
        global count
        shoe_yes()
        count = count + 5 
        spacer(5)
        print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recieves 5xp and Shoe! ")
        spacer(2)
        southpark_shoe()
        spacer(1)
   
    elif shoe_choice == "no":  
        
        shoe_no()
        count = count + 5
        spacer(5)
        print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recieves 5xp and Shoe! ")
        spacer(1)
        southpark_shoe()
        spacer(1)
    
    else:
        shoe_wrong()
        spacer(1)

# portal function 

def pright():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} heads into the right portal and they are transported elsewhere...")
    spacer(5)

def pleft():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} heads into the left portal and they are transported elsewhere...")
    spacer(5)

def pno():
    portal_choice()

def portal_choice():
    portal_choice = input ("Which one will they go into? 'left' or 'right' ")
    spacer(1)
    if portal_choice == "left":
        spacer(1)
        pleft()
        spacer(1)
        youtube_level()
        spacer(1)
    elif portal_choice == "right":
        spacer(1)
        pright()
        spacer(1)
        deathnote_level()
        spacer(1)
        
    else:
        pno()

# mumbo friend choice function

def grian():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Heads to {bcolors.GREEN}Grian's{bcolors.ENDCOLOR} location in search for the missing item")

def impulse():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR}{bcolors.RED} {bcolors.MAGENTA}Impulse{bcolors.ENDCOLOR} is in the End dimension - it will be too dangerous in there for you at this moment. Grian seems to be home though why dont you head there instead? {bcolors.ENDCOLOR}")

def iskall():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR}{bcolors.RED} {bcolors.BLUE}Iskall{bcolors.ENDCOLOR} is offline I should have remembered! You should probably head to Grian's place he should be there... {bcolors.ENDCOLOR}")

def other():
    friend_choice()

def friend_choice():
    friend_choice = input ("'grian', 'impulse' or 'iskall' ")
    if friend_choice == "grian":
        spacer(1)
        grian()
    elif friend_choice == "impulse":
        spacer(1)
        impulse()
        other()
    elif friend_choice == "iskall":
        spacer(1)
        iskall()
        other()
    else:
        other()

# Skeleton dodge game
def skdodge():
    print("You side step the skeletons arrow and counter attack with a swift punch... It falls to the ground and turns to a pile of bones!")
    spacer(1)
def skdodge_fail():
    print("The skeleton takes aim, you have no time to react! You feel a sharp pain and all fades to black...")
    gameover()
    spacer(1)
    print("Restarting level...")
    spacer(2)
    youtube_level()

def skdodge_wrong():
    sk_attack()

def sk_attack():
    sk_attack = input (f"The skeleton gets aggresive and attacks {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} do you dodge? 'left' or 'right' ")
    spacer(1)
    if sk_attack == "right":
        skdodge()
    elif sk_attack == "left":
        skdodge_fail()
    else:
        skdodge_wrong()

# Mumbo gift 
def mumbo_accept():
    global count
    print(f"You accept {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} gift... why has he give you this?")
    count = count + 5
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recieves 5xp and the dispenser! ")
    spacer(5)
    print("""
                                       .......................',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;'                                                
                                     c0XX0kkkkkkkkkkkkkkkkkkkO000000000000000000000000000000000000KWMXd'                                              
                                   .xNMWKdlllllllllllllllllllllllllllllllllllllllllllllllllllllllldONMMXd'                                            
                                  .xWMWKdlooolllllllllllllllllllllllllllllllllllllllllllllllllllloooxKWMMXd'                                          
                                 .dWMWKdloolloollllllllllllllllllllllllllllllllllllllllllllllllllllolokXWMMKl.                                        
                                .dWMWKdlolloooooollolllolllllloooooooooollloollllllllllllllllllllollooloOXWMWO;                                       
                               .oNMMXxlolllooolllllollllllllllllooooooooollollllllllllllllllllllllllllllld0WMMNx'                                     
                               lNMMNkoololllolllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllox0NMMXl.                                   
                              :NMMMNKKKKKKKKKKK0KKKKKKKKKKKKKKKKKKKKKKKKK0000000O0OOOOOOOOOOOOOOOOOOOOOOOOOOOKWMMWO'                                  
                              lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX;                                  
                              cNMMNOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOKWMMMk.                                  
                              '0MMKdllllllllllllllllllllllllllllllllllllllllllllllllllllllllollllllllllllllllxNMMWc                                   
                              .kMMKdloolllllllllllllllllllllllllllllllllllllllllllllllllllloolllooooooooollolkNMMX;                                   
                              .kMMXxloolllllllloolllllloolllollllllllllllllllllllollllloooollllllooooooolllooOWMMK,                                   
                               dMMNklooolllllllolloollooolloollolllllllllllllllllloollollloolloollllllllloolo0MMMK,                                   
                               lWMNkloollllllllllllolooooooooloollllllllllllllllllloooooooloolloollllllllloloKMMMk.                                   
                               lWMWklllollllllllolllc:::::::::lolllllllllllllllllolc::::::::clllollllllllloldKMMMk.                                   
                               :NMWOolollolllllloool,........':olllooooloolllollool,........,cololoollooloolxXMMMx.                                   
                               ,KMM0olollolllllc:::;'........',;,;:looloolllol:,;;,'........',;;,;coolllloolkNMMMo                                    
                               ,KMM0ollllllloll;..................;lollollllol,..................'collllloolkWMMWl                                    
                               'OMMKdlollllloll;........,coool,...;lloolllolol,...,clllc,........'colollllloOWMMX;                                    
                               .kMMKdlollllllol;........cXMMMXc...;lololoollol,...cXMWMXc........':ololllllo0MMMK,                                    
                               .kMMXdlolllollol;........cXMMMXc...,loloooooool,...lXMWMXl........'collllooldKMMMk.                                    
                               .xMMXxlolllollol;........;xOkOx;...';;;;;;;;;;;'...:kOOOk:........'collllloldKMMMk.                                    
                                lWMNkloollollol;........,clllc,...................,coloc,........'colllllolxXMMWo                                     
                                lWMNklooloollol;........,clclc,...................':::::'........'cooolololkNMMWc                                     
                                :NMWklooool:,;;'........'''''''...................................,;;;cloolkWMMX;                                     
                                ;KMW0olllol,......................:odddxxxxxxd:.......................;lolo0MMMK,                                     
                                ,KMM0ollloc'......................oNMMMMMMMMMNo.......................;lllo0MMMO'                                     
                                .OMM0oooooc'.................:dddd0WMMMMMMMMMW0ddddc'.................;cccoKMMMk.                                     
                                .kMM0c;;;;,'................'xWMMMMMMMMMMMMMMMMMMMMk,..................''.;OMMWo                                      
                                .kMMK:......................'xMMMMMMMMMMMMMMMMMMMMMk,.....................;0MMWl                                      
                                 dMMXc......................'xWMMMMMMMMMMMMMMMMMMMMk,.....................cXMMX:                                      
                                 lWMNo.......................dWMMMMMMMMMMMMMMMMMMMMk,.....................cXMMK,                                      
                                 lWMWx.......................ckOOk0WMMMMMMMMMWKkkOOo'.....................oNMM0'                                      
                                 :XMMk'...........................cXMMMMMMMMMNo..........................'dWMMk.                                      
                                 ,KMMO,...........................;xOOOOOOOOOk:..........................'xWMMd.                                      
                                 ,KMM0;..................................................................,kMMWl                                       
                                 '0MMXc..................................................................,OMMNc                                       
                                 .kMMXl..................................................................;0MMK,                                       
                                 .kMMWd..................................................................cXMM0,                                       
                                  dMMWx'.................................................................cXMMk.                                       
                                  lWMMOc:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::xNMWx.                                       
                                  cNMMWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWMMWl                                        
                                  ,KWNXXXXXXXXXXXXXXXXXXXXXXXXXXXK0OOOO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOO0OOkxxxd'                                        
                                                                       """)
    spacer(1)

def mumbo_decline():
    print(f"You decline the gift as you have no need for it.{bcolors.RED}Mumbo{bcolors.ENDCOLOR} tries to force it on you. You decline it again... the world around you collapses and all fades to black... it must be important...")
    spacer(5)
    gameover()
    spacer(2)
    print("Restarting level...")
    spacer(5)
    youtube_level()

def mumbo_other():
    mumbo_gift()

def mumbo_gift():
    mumbo_gift = input (f"Do you accept {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} very odd gift? 'yes' or 'no' ")
    if mumbo_gift == "yes":
        spacer(1)
        mumbo_accept()
    elif mumbo_gift == "no":
        spacer(1)
        mumbo_decline()
    else:
        mumbo_other()

#  Accept ryuks offer

def ryuk_accept():
    print (f"{bcolors.MAGENTA}Good choice, if I roll an odd number with this dice. You die. If I roll an even number. You win and recieve a gift.{bcolors.ENDCOLOR}")
    spacer(1)

def ryuk_decline():
    print (f"{bcolors.MAGENTA}Do you really want to annoy me? I am a god of death you know... shame, it could have been fun!' Ryuk{bcolors.ENDCOLOR} writes in the book... the name reads {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} - cause of death - heart attack. Time of death - in 30 seconds. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Stumbles and falls to the ground clutching their chest. Everything is fading to black... ")
    spacer(7)
    gameover()
    print("Restarting level...")
    spacer(1)
    deathnote_level()
    spacer(1)

def ryuk_other():
    print(f"{bcolors.MAGENTA}Come on kid I need an answer...{bcolors.ENDCOLOR}")
    spacer(2)
    ryuk_gift()

def ryuk_gift():
    ryuk_gift = input (f"Do you wish to take your chances with {bcolors.MAGENTA}Ryuk's{bcolors.ENDCOLOR} offer? 'yes' or 'no' ")
    if ryuk_gift == "yes":
        spacer(1)
        ryuk_accept()
    
    
    elif ryuk_decline == "no":
        spacer(1)
        ryuk_decline()

    else:
        ryuk_other()

# dice roll game function

def dice_roll():
    ran_num = random.randint(1,6)
    print(ran_num)
    if ran_num % 2 != 0:
        spacer(3)
        print(f"{bcolors.MAGENTA}Ryuk{bcolors.ENDCOLOR} rolls a odd number, Ryuk{bcolors.ENDCOLOR} writes in the book... the name reads {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} - cause of death - heart attack. Time of death - in 30 seconds. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Stumbles and falls to the ground clutching their chest. Everything is fading to black... ")
        gameover()
        spacer(3)
        print("Restarting level...")
        spacer(5)
        deathnote_level()
 
    else:
        spacer(1)
        global count
        print(f"{bcolors.MAGENTA}Ryuk{bcolors.ENDCOLOR} rolls an even number... You live another day, You've bested a god of death!!")
        count = count + 5 
        spacer(1)
        print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recieves 5xp! ")



       
 



# Start of introduction fucntion
def introduction():
    global name

    name = input("What is your name? ")
    spacer(2)

    ### Intro text
    print("""
    ░▒█░░▒█░█▀▀░█░░█▀▄░▄▀▀▄░█▀▄▀█░█▀▀░░░▀█▀░▄▀▀▄░░░░░░░░░
    ░▒█▒█▒█░█▀▀░█░░█░░░█░░█░█░▀░█░█▀▀░░░░█░░█░░█░▄▄░▄▄░▄▄
    ░▒▀▄▀▄▀░▀▀▀░▀▀░▀▀▀░░▀▀░░▀░░▒▀░▀▀▀░░░░▀░░░▀▀░░▀▀░▀▀░▀▀""")
    spacer(1)

    print("""
    ░▀▀█▀▀░█▀▀░█░░█▀▀░▒█░░▒█░▄▀▀▄░█▀▀▄░▀█▀░█▀▀░█░█░▄
    ░░▒█░░░█▀▀░█░░█▀▀░░▒█▒█░░█░░█░█▄▄▀░░█░░█▀▀░▄▀▄░░
    ░░▒█░░░▀▀▀░▀▀░▀▀▀░░░▀▄▀░░░▀▀░░▀░▀▀░░▀░░▀▀▀░▀░▀░▀""")

    print("""
    ░▀▀█▀▀░█░░░░█▀▀░░░█▀▀░█▀▀▄░░▀░░█▀▀▀░█▀▄▀█░█▀▀▄░▀█▀░░▀░░█▀▄░░░▄▀▀▄░█▀▄░█░░█░█▀▀░█▀▀░█▀▀░█░░█░█
    ░░▒█░░░█▀▀█░█▀▀░░░█▀▀░█░▒█░░█▀░█░▀▄░█░▀░█░█▄▄█░░█░░░█▀░█░░░░░█░░█░█░█░█▄▄█░▀▀▄░▀▀▄░█▀▀░█▄▄█░▀
    ░░▒█░░░▀░░▀░▀▀▀░░░▀▀▀░▀░░▀░▀▀▀░▀▀▀▀░▀░░▒▀░▀░░▀░░▀░░▀▀▀░▀▀▀░░░░▀▀░░▀▀░░▄▄▄▀░▀▀▀░▀▀▀░▀▀▀░▄▄▄▀░▄""")
    spacer(1)

    ### Print out the introduction to the game (3rd person)

    print(f"After sitting up all night, programming and wiring their RaspberryPi so it can work as a TV remote. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} figured they would have a go at getting it to work.")
    spacer (1)
    print(f"An odd face appears and a strange static emits from the screen... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides to ignore it, thinking it was nothing but the boot menu logo for the RaspberryPi.")
    spacer (1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} now has access to all streaming services and channels, but something is off, something went terribly wrong. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} has no idea whats coming...")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides its time to rest on the distressed looking couch that they are familiar with falling asleep on from time to time when binge watching rubbish.")
    spacer(1)
    print(f"Tonight will be more interesting than {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}'s usual night...")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides to do the usual... binging their favourite shows!")
    spacer(1)
    print(f"After some time binging {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} feels sleepy, they decide to rest.")
    spacer(1)
    print (f"Whilst sleeping the strange static consumes {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}")
    spacer(3)
    print("""
                        ...',.  .:. ;ddddooollc;.                                                                                                  
                    .;ldxkOKXNNWNk:,xd.lWMMMMMMMMMWO'                                                                                                 
              ...'lOXWMMMMMMMMMMMMNx,;:'dWMMMMMMMMMNl,c'                                                                                              
             .:lkXMMMMMMMMMMMMMMMMMWk';:'xWMMMMMWKolkNMK:.                                                                                            
           'dKWMMMMMMMMMMMMMMMMMMMMMWo.dd,cKNKko::lOWMMMK:.                                                                                           
          :XMMMMMMMMMMMMMMMMMMMMMMMMMx.:k:.'cccokXMMMMMMWl.,.                                                                                         
         .xMMMMMMMMMMMMMMMMMMWX0kdlcc;',:ldOKNMMMMMMMMMMMO';c                                                                                         
         .OMMMMMMMMMMMMMWXOdc:cccodkO0XNWMMMMMMMMMMMMMMMW0;.l;           ....................................''''''''''...........',,,,,,;::;.        
         .lkkkkkkkkxdlccccclx0NWMMMMMMMMMMMMMMMMMMMMWKxl:cl''c;,,,;;;;;;;;;;;;;;,,,'',;;,;;;;;;;;;,,,''.''''',,,,,,,,'...................cKMWx.       
          ,oxkxl:cccldxOKXWMMMMMMMMMMMMMMMMMMMWNNKko::cx0NWo.                               ...................'',,,,,,,,,,,,,,,;;;;::::o00x0d.       
         .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kl:ccc:coONMMMMMk.'dddddooooddddddxddooooooooooooooddddooooooooooooooooddooooooooooolccccccck0l.'x:        
          .odxOXWMMMMMMMMMMMMMMMMWXKOdoc;.':oOKXNNWMMMMMMMMk..''''''.......................                                           .l:  :d.        
               .,:cloddxkkkkkkxdc;'. .:xkkKWMMMMMMMMMMMMMMMO.  .,,,,,,,,,,,,,,,,,;:;:::::::::::::::::::::::::::::::clllllllllllll,    ,d' .dc         
                                      oWMMMMMMMMMMMMMMMMMMMO.  .cldKNNNNNNNWWWNx:cOWMMMMMWXOKWMWMMWWN00XWWWWWMMMMMMMMMMMMWXkl:oKMk.   co  ,x,         
                                      .xWMMMMMMMMMMMMMMMMMMk.      'xXWWWWWMMMXc  .lXMMMM0, .xWMMMW0:. cXWWWWMMMMMMMMMN0d:.   .kWl   .d;  co          
                                       '0MMMMMMMMMMMMMMMMMM0'.;'     :0WMMMMMMMXl.  ,dkkkc   ;OO00d.  .xWMMMMMMMMMWKxc'.  .'cx0W0,   :d. .o;          
                                        dMMMMMMMMMMMMMMMWWMWd.lKx:.   .ckNWWNKkdc'.   .:l'   'cc:.   .;dxkKNWMWXkl,.   .:d0NMWWWd   .oc  :o.          
                                        cNMMMMMMMMMMMMMNo;:ll..xOl.      ':c::;:lxkl.  ;Oc   lKx'  .:ddoc::clc;.   .,lkXWMMMWWWX;   ,d' .l:           
                                        .OMMMMMMMMMMMMMW0xoc,. .             .;kNMWNd'.,c'   ;d:  .dNMMNkc'.    .;xKWMMMMMMMWWWx.   lo  ,o'           
                                         lWMMMMMMMMMMMMMMMMMNO,  ,c:,.         .;okxlcldd,  .cdl:,:lool,.   .:l::oONMMMMMMMMWWNc   .d;  cc            
                                         ,KMMMMMMMMMMMMMMMMMMWd.:XMWNX0xl,.        .;xXWN:  .OWNX0d'     .;xXWMXxcckNMMMMMWWWWO.   :d. .o,            
                                         .kMMMMMMMMMMMMMMMMMMMXddNMMMMWKd,....       'kWW0lckNMMMMKc.,col:cdKWWKd;.'clc::;,,dXo   .dc  ;l.            
                                         .dMMMMMMMMMMMMMMMMMMMMMMMMWKd;.,oOXXd.  ckl;cKMN0xdddxkO0NWXNWWN0oclOx.           .ck,   ;x' .l:             
                                          cNMMMMMMMMMMMMMMMMMMMMMXx:',lkXMMMWk.  :NWWWMWXkddddol::l0WMMWWMNxcldl::,..cdxkOO0Nd    lo  'l.             
                                          .kMMMMMMMMMMMMMMMMMMXkc''ckNMMMMMMWo   oWMWWMMWWWWMWWN0l;:::;;;::,..'cddc''lxxkOkkk,   .d;  ::              
                                           ,0MMMMMMMMMMMMMMXxc,,ckXWMMMMMMMMK:....cOWWWMMMMMMMMMNd'.                              .   ..              
                                            cNMMMMMMMMMMNOl'.:xXWMMMMMMMMM0o, .'.  :XWWWWWWWWMMMXc                                                    
                                            .xWMMMMMMMMMKc:xKWMMMMMMMMWXOo'    .:::cox0KK0XWWWWNd.            .. ;o'      ;:.   .;.  ..               
                                             .kWMMMMMMMMWWWMMMMMWNKOdc,.       oWNx::cc;..,oddo,           'ld0x..k0,     lc    oo  'c.               
                                              .l0WMMMMMMNKOxdlc;,'.   ..      'kO:. .x0;   :xc.    .oO; ...kMMMWk..k0xc.       'x:  :;                
                                                .,:clc:;'.           .'      .''   .oXNl  .ld'   ..dWWl ::.lNMMMWk..kWW00k,    cx. .c'                
                                             '.   ;xc.     .,c:.   .:,..     ..  .';lod,          ;KMWl dO..OMMMMWO'.xWMMWO.  .lc  ;:                 
                                           ,k0;  'OMk'..;okKXx.   'kkcdl.      .l0KOkdo,         .xWMN:.xWl cNMMMMWO'.dNMMWx.  .   '.                 
                                          .kMx.  ,0NNKOKNNNO;    :0XNNX:    .oxONNNNNNX0d.    .  .kMMX;.kMK,.xWMMMMW0,.dWMMNo                         
                                          :XX:    .''''''''.     .''''.      .''''''''''.         lNMX;.kMWx.,KMMMMMMK;.dWMMK,..                      
                                         .xWk.                                                    .kMK;.kMMNc.oWMMMMMM0;.oNMN:                        
                                         ;XX:                                                      oMK;'0MMMO.,0MMMMMMMK:.lNWo                        
                                        .dWXdcccccccc;.    ';;:::;;;;,.   .',;;;;;;;;.    .;'      cWK,,KMMMNl.lNMMMMMMMK;.cXx.                       
                                       ,kK0OOkkkkkOOk;    .dkkOOOkO00k'   'okKKKKKKKk,   .dKl      ;XO.;KMMMM0'.kMMMMMMMMX:.co.  .                    
                                     ,xKk;. ,lc;;:'.    .,;c:;;;;:cc:,    .;:::c:::,.   .,:;.      '0k.;KMMMMWd.cNMMMMMMMMXc.. .l,                    
                                   ,xXO:  .okd;:o:.      'll'..'co;...    ...;dl'''.    .,c;       .Ok.;KMMMMMNOKWMMMMMMMMMXc  ..  .;oxx:. ,,.        
                                 ,xXO:. .lOOl':o,    .'',od;''':d:'..     ..'ll'..     ..;c.       .kk.:NMMMMMMMMMMMMMMMMMMMNl   .lKWMMMWx,cKk'       
                               ,xXO:. .lxo,.....     .'cdc,,,:dl,''';.    ;xdc;,;,    .,oo'        .xN0KMMMMMMMMMMMMMMMMMMMMMk. .kWMMMMMMMXXWM0'      
                             ,xX0:. .lkkl;;c;,'    .',:dl;,,;oo;''.,o;   .lkl''''.   ..co,...       oMMMMMMMMMMMMMMMMMMMMMMMXc ,xXMMMMMMMMMMMMWO.     
                           ,xX0c. .ldc...,c:....    .ll,...co;....:o:.   .,,,';o:    'do;;;;'    .. ;XMMMMMMMMMMMMMMMMMMMMMMx.'0MMMMMMMMMMMMMMMWd.    
                         ,xX0c. .lkkl;,;col,';ol;,,;odc,,,cdl,,,';oc.     .'''cl.   .oo;'..;,    ....oWMMMMMMMMMMMMMMMWNXKko' cNMMMMMMMMMMMMMMMMNc    
                       ,xX0c. .oKk,...,l:...:l,...;o:...,ol'.........     .''',.   .lc,,,,ld.    'oc.'0MMMMMMMMMMMMXd:c::::o: ;KMMMMMMMMMMMMMMWKo.    
                     ,xX0c. .oKXd,. .,:.   ;:.   .c'   .:;                         ;'    ,:.     ;;  .dWMMMMMMMMMMMN0OKXXNWMo..;oO0KXWWWWWX0xoc;cc.   
                   ,xX0c.  ,0WMNK00O0Kxoook0xooloOOdoookkolll::c:ccc,.   .cll,    ,olllldko;.   ,o:;;.;XMMMMMMMMMMMMMMMMMMMMo.oOl:ccccc:cccccokKWO.   
                 'xX0c.    .,:::::::::::::::::::::ccllllloxkkkkkkkkkl.   :OOOc    'loooooodc.   ,oddo..kMMMMMMMMMMMMMMMMMMMMk.lWMWWNX0kdddkOXWMMM0'   
               'dX0c.                                   .lKXKKKKKKKKx.  .kXXXc                         ,0MMMMMMMMMMMMMMMMMMMO':NW0dc:cccccccc:co0K;   
             'dX0c.                                    ,OXx;'''''''''.  .kWMK;                          ,0WMMMMMMMMMMMMMMMMMO.c0l,cxOKNWWWWWNKkc;;.   
           .dX0c.                                    .dNWOc;;;;;;;;;;::cdXXk:                            'OMMMMMMMMMMMMMMMMMk..';0WMMMMMMMMMMMMWKl.   
         .oKXd'.....                                 ,k000000000000000000k;.                              'kWMMMMMMMMMMMMMMMO. ,0MMMMMMMMMMMMMMMMX;   
        :KMMN000000000000000OOkkkkkkkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOkkOkOkxxxdoddddddddddo'    :ooooooooxOo'lXMMMMMMMMMMMMMMk. oWMMMMMMMMMMMMMMMMK,   
        oWXd:::::::::::::::::::::::::cclllllllllllllollolllllllllooooooooooooooooooooooddd,   .:xdxxxx0WWOdd;;OWMMMMMMMMMMMWx.,KMMMMMMMMMMMMMMMMMk.   
        ;XX:                                                                                          ,KNxxNx..ckKNMMMMMWXkl' .OMMMMMMMMMMMMMMMMWl    
        .OW0ooooooooooooooooooooooooooooooooooolccccccccccccccccccccccccccccccccccccccccccccccccccccccdXWWNx.    .,:ldol:'.    :NMMMMMMMMMMMMMMMK,    
         ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkOOOOOOOOOOOOOOOOOOOOO00000000000000O0XXo.                   .xWMMMMMMMMMMMMMMk.    
                                                                                                        ..                      ,KMMMMMMMMMMMMMXc     
                                                                                                                                 lNMMMMMMMMMMMXl      
                                                                                                                                 .oNMMMMMMMMWK:       
                                                                                                                                   ;xKNWMWXkc.        
                                                                                                                                     .',;;.           """)
    spacer(5)
    southpark_level()
    
# Southpark level fucntion start
def southpark_level():

    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} wakes up, something isnt right... they are somewhere theyve seen before. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} looks around and tries to make sense of the location. They are in the show they were watching before they slept! Which is....")
    spacer(5)
    print(f"""
    .▄▄ ·       ▄• ▄▌▄▄▄▄▄ ▄ .▄ ▄▄▄· ▄▄▄· ▄▄▄  ▄ •▄  ▄▄ 
    ▐█ ▀.  ▄█▀▄ █▪██▌•██  ██▪▐█▐█ ▄█▐█ ▀█ ▀▄ █·█▌▄▌▪ ██▌
    ▄▀▀▀█▄▐█▌.▐▌█▌▐█▌ ▐█.▪██▀▀█ ██▀·▄█▀▀█ ▐▀▀▄ ▐▀▀▄· ▐█·
    ▐█▄▪▐█▐█▌.▐▌▐█▄█▌ ▐█▌·██▌▐▀▐█▪·•▐█▪ ▐▌▐█•█▌▐█.█▌ .▀ 
    ▀▀▀▀  ▀█▄▀▪ ▀▀▀  ▀▀▀ ▀▀▀ ·.▀    ▀  ▀ .▀  ▀·▀  ▀  ▀ """)
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} walks around for a while and bumps into some familiar characters, you bump into {bcolors.BLUE}Kyle{bcolors.ENDCOLOR} and {bcolors.MAGENTA}Cartman!{bcolors.ENDCOLOR}")
    spacer(1) 
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} approaches the gang and sees they are messing aorund with chinpokemon. They see {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} and engage in conversation. They chat away and offer {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} their very own chinpokemon!")
    spacer(1)
    chinpokemon_choice()
    spacer(1)
    print(f"Sorry about {bcolors.MAGENTA}Cartman!{bcolors.ENDCOLOR}, {bcolors.BLUE}He doesnt like sharing! Here, take this as compensation... it's not much but its something....{bcolors.ENDCOLOR}")
    spacer(1)
    shoe_choice()
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recieves a beaten lookng Shoe...")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} reluctantly thanks {bcolors.BLUE}Kyle...{bcolors.ENDCOLOR} {bcolors.BLUE}Kyle{bcolors.ENDCOLOR} and {bcolors.MAGENTA}Cartman{bcolors.ENDCOLOR} decide to head off to meet their friends and just as they do, 2 portals open!")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} is curious and heads towards the 2 portals...")
    portal_choice()

# Final-level fucntion start
def final_level ():
     
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} enters a new realm... they look around, trying to gather their bearings and figure out where they have ended up this time... ")
    spacer(5)
    print("""
    ▄• ▄▌   ▐ ▄   ▄ •▄    ▐ ▄           ▄▄▌ ▐ ▄▌   ▐ ▄    ▄▄   
    █▪██▌  •█▌▐█  █▌▄▌▪  •█▌▐█   ▄█▀▄   ██· █▌▐█  •█▌▐█   ██▌  
    █▌▐█▌  ▐█▐▐▌  ▐▀▀▄·  ▐█▐▐▌  ▐█▌.▐▌  ██▪▐█▐▐▌  ▐█▐▐▌   ▐█·  
    ▐█▄█▌  ██▐█▌  ▐█.█▌  ██▐█▌  ▐█▌.▐▌  ▐█▌██▐█▌  ██▐█▌   .▀   
    ▀▀▀   ▀▀ █▪  ·▀  ▀  ▀▀ █▪   ▀█▄▀▪   ▀▀▀▀ ▀▪  ▀▀ █▪    ▀   """)
    spacer(3)
    print("After looking around for some time they see something familiar - It's a green pipe from Mario! ")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides to enter the pipe, they figure its just like the game and they will be transported elsewhere. ")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} gets sucked into the pipe like a vortex, they are dumped into a dark and cold alleyway somewhere within this realm...")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} looks towards the end of the alleyway and makes their way out, they see some familiar looking figures, something seems off about them.")
    spacer(1)
    print(f"They take a second look at the familiar figures and realise who or what they are... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} gasps in complete shock! ")
    spacer(1)
    print(f"{bcolors.YELLOW}'Is that... sonic with human teeth? And... Deadpool but the really bad version from Fox? Wait a second... is that Baymax? Why does he look like a pig?...'{bcolors.ENDCOLOR}" )
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} makes sense of where they are, they are in the recycling bin of the internet... where big dreams end up when they shouldnt have existed in the first place. A few hours pass and {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} continues on exploring the realm and finds a small nook. There is a red glow emitting from the wall... it looks familiar, Is that redstone?" )
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} approaches the strange glow and realises there is message inscribed on the wall. {bcolors.YELLOW}'Has Mumbo been here previously?...'{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"The message reads - '{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} {bcolors.RED}Touch the text, all will come together... Good luck'{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} touches the red text and a strange aura surrounds them. A portal appears and the items they have collected along the way fly into it and form into...")
    spacer(1)
    print(f"{bcolors.GREEN}⚡THE SOLE SENTRY OF THE APPLE EMPIRE⚡{bcolors.ENDCOLOR}")
    spacer(1)
    print("""                                                                                                                     'cc:,.  ,x;                                                                       
                                                                                                                  .:dOKOxkK0o;dkd;                                                                      
                                                                                                              .:ok0Oxoll::lolxk;:d,                                                                     
                                                                                                          .:okK0xoolokKOllkocko''lxclc'                                                                 
                                                                                                      .;lkK0xollodOKKKOdkOddoxdccdkllOKOo;.                                                             
                                                                                                 .,lokK0xolllx0KOllkK0dxxcododxddxxxdllox0Kkl'.                                                         
                                                                                             .:lx00xdolloxOKKKK0dodokxdx:.;ddk0OO0KKKK0kollok0Oxc'                                                      
                                                                                         .'lxKKkdolooxOKKKKKKKKxdl;oolddcclxdd0KKKKKKKKKKKOdolldOKOo;.                                                  
                                                                                      .:x00kdolodOKKKKKKKKKKKKkoo;.;dxxxxxxxk0KKKKKKKKKKKKKKK0kdloox0KOdl,                                              
                                                                                    .d0WWk,'ckKKKKKKKKKKKKKKK0odx;';xxoOKKKKKKKKKKKKKKKKKKKKKKKOdc,;kWWWWX:                                             
                                                                                    :XXoloodollox0KKKKKKKKKKKKOdooldxdkKKKKKKKKKKKKKKKKKKKKOdlclokKX0dl:xNc                                             
                                                                                    ,Kk,:oloodddoollodOKKKKKKKK0OxdxOKKKKKKKKKKKKKKKKKKOdlcloxKX0dollox;cXo                                             
                                                                                    ,Kk,dXKOdlloodxddollldk0KKKKKKKKKKKKKKKKKKKKKKKOdlclokKX0dollok0KKKc,0k.                                            
                                                                                    ,KO,oKKKKKKOxolloodxxdollox0KKKKKKKKKKKKKKKOdlcloxKX0dollox0KKKKKKKo,k0'                                            
                                                                                    '0O,lKKKK0OkO0K0OxollodxxdooloxOKKKKKKKOdlclokKX0xollok0KKKKKKKKKKKd,xk'                                            
                                                                                    '0O,lKKKKd,,::ckKKKK0xollodkkxollldxdllloxKXOdollok0KKKKKKKKKKKKKKKk,,xOl.                                          
                                                                                    '0O'cKKOl,.;:::xKKKKKKKK0kollodkOkdloxKXOdollok0KKKKKKKKKKKKKKKKKKKO:lkdkd.                                         
                                                                                    .O0':KO:.,c:;::kXKKKKK0xoxk00kolloo0Xdcllok0KKKKKKKKKKKKKKKKKKKKK0kxxl'.cX0,                                        
                                                                    .ol':d;  ''     .k0,cXx;';kx;;;cdx0KK00:.',;cOKKKx'cK:;0KKKKKKKKKKKKKKKKKKKKKKKK0dk0l..,kWKk:                                       
                                                                 ...lWKONX: .Ok.    .dOclOd:,';dc';,''oKdc:,,::,'lk0K0;cXc:0KKKKKKKKKKKKKKKKKKKKKKKOdkx;..;kOc.l0:                                      
                                                                'kO,oNKNOxx';KK,  .:ccllccc:'.',,',,,'co:::;;;;:;''oK0:cXc,0KKKKKKKKKKKKKKKKKKKKK0Okxc,;',Od,:;,k0;                                     
                                                            :l..kNo.dddNl;Oll00l .xk,;cccclllc:;;;;;;:;'';;;;,;:l:.:0Kc:Xl,OKKKKKKKKKKKKKKKKKKKKOxkx;,o;'xo'lxx:,k0,                                    
                                                          .oXl ckOo;k:.l::Oko,oOlOWd'lxxxxxxxxxoc,.'':dkdc,'.:dkkc'oKKc;Ko,OKKKKKKKKKKKKKKKKKK0xkkc,:dl.lo,lxxxx;,Od.                                   
                                                         .lxOl:x,'xXk.   ,xl. cN0kNd'lxxxxxxxxxdc''''.'d0KOolc;,,,'dKKl'Od,kKKKKKKKKKKKKKKK0kddkd;;oxx,,d;;xxxxxo'lK:                                   
                                                         ld.;0O,  .c,         cKxkWd'lxxxxxxxxd;...',,oKKxlcclc:c;';ckd,kd,kKKKKKKKKKKK0kdl::dkc,cdxxo':d':xxxxxx:'k0'                                  
                                                     .;. dx..l:      ..       .'dWMo.lxxxxxxxx:...,0WNWMMx'lc..:col;'dx,xd,kKKKKKKK0kdlc;,,oOo,:dxxxxl'ol'oxxxxxxd,;0l                                  
                                                     'Ok;o0;  ...,,',::::c:,.  .kWWd'lxxxxxxxx:.'..:lkWMMNkOx.,dl:cclxo,xx,dKKK0kdl:;,;;cdxl,,lxxxxxx;,xc,dxxxxxxxl.l0;   ..                            
                                     ..  ..          'OOcll''xOO0KXXkdOKXK00Oo'.cdKo.lxdxxxocc:'';'  ;XW0kKNo.;dxxc.oKo;okkxdll:;,;:;,:dxc,,cdxxxxxxx;'kc,dxxxxxxxo',0k..co;                            
                                    ,Ok:o0c .;,      .cd,  .xX0OkO0KKKXKOkc,lK0' ,00lcccc::codl..;c;';lc,..,',oxxo,:0k:dXNW0c;;,,,;ldol:,;oxxxxxxxxxx:'d:,dxxxxxdlcl,oN0d;        .,.                   
                                 ',.oMX0KXl '0O.    .cdkKl .OXkkkkkkOkkOkOx,;O0,'OWMMWWNNXKNMMWO:dXWNWNKKOc',;:::,;00,.,:dKd.,:;;clc:;,:dxxxxxxxxxxxx;,kc,dxxdllodkO;;XXc     .'.,xo.                   
                             .  :Kk'dX0Kdok,,KK;    .dklxd. oX0kkkkkkkkkkOxloOc,dkk0XNWMMMMMMMMMMMMMMMMWK0KKOOkxdkXMXc,;,,,lo;,::;;:ldxxxxxxxxxxxxxxx;'kd.coloxO000O;:XMX:   ;xocl;.                    
                           .do.,KNc.kdoNd:kclxko.,'  .:lc,  .xKOkOkkOkkOkOkk0l'xk,...,:coxO0XNWMMMMMMMMWd',:cllldk0XWN0dc:,.;oc;lxxxxxxxxxxxxxxxxxxxxl.c0:'ok000000o,dWMM0' 'kc                         
                          .kXc.xkxdoO; ;':0Ol.lOkKO,   .;lc;..oK00KKK0OOkOOx::kOxoc:;,;:;'...,:lodONMMMMXc'c:,,::ccclokXWXx:..ox;;ldxxxxxxxxxxxxxxxxdl,.xx,o000000k;cXMMMWO,cx.                         
                         'olxxld'.dXd.   ,d;  lNOox,   .cdxKKc;cdKWWNX0O0kc,lOl.';;:cccllllddl:;'..xWWMMMKllkOl,lxxxoc::o0WNk:'cxd;;oxxxxxxxxxxxxdolloxc;k::0000Ol:xXMMMMMM0kc                          
                         od.,KO.  .;.         ,xkx;     .cxXWNKo,;coxkkxl;lkOkkdlcc::clolc:cldkkxxOXMMMMMMNd;:::dxxxxxxo:;cdKWKd:lko;:dxxxxxxxxdoodk00Kx,dk;:docco0MMMMMMMMWk'                          
                     .o; ok. ''      ..        .dx,.      .lOKWMNKkxoooxO0d,,:;oNWXOxoll:;col::::ccllodOXNXXkl:clxxxxxxxxdl;;o0WXxOWKc,lxxxdollox0000000l;k0dlokXMMMMMMMMMMWl                           
                     'OOco0:  .;clc:,',cdxxo,. .k0OO,  .;:..,:lodkKNMMMMMW0oclcdNMMMMMMWXkoc::clodolc,..,;:ccokkdccokkxxxxxxoc:cxNMMMNd;:loodxk0000000Oo:;kWMMMMMMMMMMMMMMMMx.                          
                     .xo;cc..d0KKKXXdlk0OOKXKO:.;;dx,;dOx:...','.';cldk0XWMMWWWWMMMWK0XWMMMWKOdoc::,'''';oxxoc:cdkxolldxxxxxxxxl'lNMXo::',d000000000Od:ckXWMMMMMMMMMMMMMMMMM0'                          
   ,:..l;   .        .ld:   oXOkkO0KKXX0o;ckOKK; '00OXKkdolc:;,....''..';coxOXWMMMXl';ccdxxkO0KXNKkc'',cdxxxxxxoc:ldkxlcoxxxxxxxc'dWX:,c,,;x0000000d:cOWMMMMMMMMMMMMMMMMMMMMk.                          
. ,KKokXl  cx.      .xOOXl .xXOkkkkkkkkkOo.;kK0;.xNX0kxxxxxxxxddlc:;,........':ldOOxol:..';:::;';oo,.;dxxxxxxxxxxxo::ldxolc:cldoc,,OMx,oc;:,d00kooccxNMMMMMMMMMMMMMMMMMMMMMW0,                          
k':XKKxdo..xX;      .dkloc. cK0kkkOkkOkkkc'lkOc,x0kxxxxxxxxxxxxxxxxxxdlc:;,........,:odoooc::;,..,:lddxxxxxxxxxxxxxxxl::oxkkdl:,:;;0MO,oO:cl,cc:lx0NMMMMMMMMMMMMMMMMMMMMMXxckd. .lk;                    
x.lxdXd'dc,kKo        ,cc,. .oKOkkOOkkkOxco0O::kOxxxxxxxxxxxxxxxxxxxxxxxxxddlc:;,'......,;cokOl.:xxxxxxxxxxxxxxxxxxxxxxdl::lxkkxxkXWXc,kKl;kl,dKMMMMMMMMMMMMMMMMMMMMMMWKo.  .odldodk' .:;.              
o.dc.lc'dxo:lx;lo'      ;ooo:'cO00KXK00Ok00d''OKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoc:::;,'.,kKl.'lxxxxxxxxxxxxxxxxxxxxxxxxdllollllooolcd00:,ONNWMMMMMMMMMMMMMMMMMMMMMNk:.      ,c, .oOoc.                
dkx'   .dx, ;Okoxc     .okOXNo..:kXWWWNK0x;.;xOkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxolc::ccccllc:codxxxxxxxxxxxxxxxxxdlok00000kxdk00koloONMMMMMMMMMMMMMMMMMMMMMMXd,              .,'                  
.o;     ..  ,Kkld'      .,c:;cclooxOdodoc;ck0Oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl::clccclcc:coxxxxxxxxxxdollxO0000000000xllxXWMMMMMMMMMMMMMMMMMMMMMW0l.                                     
   ...       'lk;              .cKNKkoodxkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl::clcc:clc:coxxxxdccdk0000000000OoclkNMMMMMMMMMMMMMMMMMMMMMMNkc.                                       
.  ;l,....    l0dl.            ;OXOxxxkkxdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddl:;:c:::cc:::cok0000000000xlld0WMMMMMMMMMMMMMMMMMMMMMMXd,                                          
xx:,lkOOOkxc. :ddk;          ,kXXkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl:::::c::looooooooollllkXMMMMMMMMMMMMMMMMMMMMMMWWk'                                            
O0OxkOOd:lkKO'  co.         cXXOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd:clllccllllllclONNWMMMMMMMMMMMMMMMMMMMMMMNx:dx.                                            
OOxxxkOx'.dOKc ;d'         cXXkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdld000kxxxxxxxxo,dMMMMMMMMMMMMMMMMMMMMMMMNx,  .co'       ..:l'                               
kkOOOkOo;cxO0l:o'         'ONkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxocd000000000000xdkXMMMMMMMMMMMMMMMMMMMMMXd,      ckc'.,:locc:xx..,cl,                         
kkOkkOkxxxkOddo.      .'..dXOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdlcx0000000000kdx0KWMMMMMMMMMMMMMMMMMMMW0l.         ,llccc;.  .xKxoc;d0,.:o,                    
00OOOkkOOkdokx.    .:loOxkNKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlcO00000000OddkKNMMMMMMMMMMMMMMMMMMMMWOc.                    ;xc'..  .xOdc.                     
XXXXKOO0x;.;x:      ''.;KMXkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdolcllok0000000kkkkXWMMMMMMMMMMMMMMMMMMMMNk;.                     .xd.      .,.                       
lx0KXXkl,;ol'    ,coc. ,0KkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdollooodkO000000kxkOKWMMMMMMMMMMMMMMMMMMMMMKd,                         .co;.                              
:coddxdcc:'     'c;ok,.OKc;oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoollldxk000000000Oxxk0WMMMMMMMMMMMMMMMMMMMMMWKd.                             .dd.                             
  .';:,.           ,O:cNkodlcoxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddoollolldxkO0000000OkkxkOOXWMMMMMMMMMMMMMMMMMMMMMNkcxx.                             .xx.                             
                   .xc:0xxKOdlclodxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddddooollloooooddddxO0000000OkxkkOkO0KNWMMMMMMMMMMMMMMMMMMMMMWKd,  oO.   ..              .:c,.     ,0c                              
                    :ok0oxK000kdlolcloodxxxxxxxxxxxxxxxxxxxxdoollloodxdooddddxkOO0000000000OxxxkkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMNkc.    lO:;lkO,              .,;ldl,.  cx.                              
                      lKdxK0000000kxdooollllccclooooodooooooooodxkO0000000000000000000Oxxkkk0KNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo'       :ko;,kx.                   ,coc,xd                               
                      cXkxkxxkk000000000OkkxddoodddddddxkkOO0000000000000000OOkkkddkOOOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;.          .  ck;    .                 .;kXd.                              
                      ;KMWX00OxkOkxdddxkO00000000000000000000000000000OkkxxxkOOOOO0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd:.               '0d   .oko,                 l0ooc.                            
                      .kMMMMMMMMMWNK0OOkkkkxkxkkkO0000000000OxxkxxkkxxxkO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKko;.                 .dkdo;;do',xd.               :kc'c;                            
                       lWMMMMMMMMMMMMMMMMWNXKK00kO0000000000OO0XXXWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKxoxk,                   .xd..;ll,   .;.                ..                               
                .ol,.  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc'.  .do...'.              .xd;'.                                                          
                l0lox,  lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0dc,.       oo'cll;.              .,dO;                                                          
                cO'.xx. .ckXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKxooc'.           ;xo.                    ;k,                                                          
                ok. .xl. .cdokNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdc'.                  .o,                    l0,                                                          
      ,c. .;.  ,Oc   .clcxx'  ,oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dc;.                                              'xo.                                                         
      .ox',Kx..oo.     ,0d.     .,okKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl;'                                                    .od.                                                        
        :dx0O,:d.       ,ll,        .'cdx0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0XNxc,.                                                         .lkd.                                                      
         ,:'cxkc          ,kl.           .':oxdxk0KXXNMMMMMMMMMMWWWWWNX0ko:,.'xd.                                                              co.                                                      
             ',            ,x:                    ...';;:ccc;;;;;,,,,'..     ;x'                                                                                                                        """ )
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} gets knocked back by a shockwave, knocking them back by a few feet.")
    spacer(1)
    print(f"{bcolors.GREEN}⚡THE SOLE SENTRY OF THE APPLE EMPIRE⚡{bcolors.ENDCOLOR} prepares to fight... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} readies themselves!")
    spacer(1)

    boss_choice()
    spacer(1)
    boss_choice2()
    spacer(1)
    boss_no_choice3()
    spacer(1)

# Youtube level fucntion start
def youtube_level():

    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} steps out of the portal they just entered... They look around to figure out just where exactly they have ended up")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} realises that everything is pixelated and blocky... is this")
    spacer(5)
    print("""
    • ▌ ▄ ·. ▪   ▐ ▄ ▄▄▄ .   ▄▄· ▄▄▄   ▄▄▄· ·▄▄▄▄▄▄▄▄ ▄▄ 
    ·██ ▐███▪██ •█▌▐█▀▄.▀·  ▐█ ▌▪▀▄ █·▐█ ▀█ ▐▄▄ •██   ██▌
    ▐█ ▌▐▌▐█·▐█·▐█▐▐▌▐▀▀▪▄  ██ ▄▄▐▀▀▄ ▄█▀▀█ █  ▪ ▐█.▪ ▐█·
    ██ ██▌▐█▌▐█▌██▐█▌▐█▄▄▌  ▐███▌▐█•█▌▐█▪ ▐▌██ . ▐█▌· .▀ 
    ▀▀  █▪▀▀▀▀▀▀▀▀ █▪ ▀▀▀   ·▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀  ▀▀▀   ▀ """)
    spacer(1)
    print(f"There is a structure in the distance {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides to head towards it. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} peers into the window and sees their favourite Minecfart YouTuber...  {bcolors.RED}MUMBO JUMBO!{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"It looks like {bcolors.RED}Mumbo{bcolors.ENDCOLOR} is making an intro to his video - {bcolors.RED}'Hey guys! {bcolors.RED}MumboJumbo{bcolors.ENDCOLOR} here - todays episode of this lets play is ab-'.{bcolors.ENDCOLOR}  {bcolors.RED}Mumbo {bcolors.ENDCOLOR} pauses as he sees {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} peering into the window")
    spacer(1)
    print(f" {bcolors.RED}Mumbo{bcolors.ENDCOLOR} asks {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} how they got here and who they are. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} explains the situation to Mumbo.  {bcolors.RED}Mumbo{bcolors.ENDCOLOR} sees this as an opportunity for {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}'s help.")
    spacer(1)
    print(f"{bcolors.RED}'So {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}, {bcolors.RED}I'm missing a key item for a build in my world. I'm sure that one of my friends have the missing piece, could you go and collect it for me? Maybe I can help you get back to reality after...'{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"{bcolors.RED}'Im sure they all have the items I need, its up to you who you wish to visit... you can visit either - {bcolors.GREEN}Grian{bcolors.ENDCOLOR},{bcolors.MAGENTA} Impulse{bcolors.ENDCOLOR} or{bcolors.BLUE} Iskall.{bcolors.ENDCOLOR} {bcolors.RED}I'll mark their locations on this map'{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} accepts {bcolors.RED}Mumbos{bcolors.ENDCOLOR} propositon and decides to head to...")
    spacer(1)
    friend_choice()
    spacer(1)
    print(f"After some travelling {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} arrives at their destination. They search arround for {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} friend-{bcolors.GREEN}'Hello there stranger! I assume you're new around here? Did {bcolors.RED}Mumbo{bcolors.ENDCOLOR} {bcolors.GREEN}send you... He must have! Hes the only one that know where I am haha! I'm{bcolors.ENDCOLOR}{bcolors.GREEN}Grian{bcolors.ENDCOLOR}{bcolors.MAGENTA}, pleased to meet you.'{bcolors.ENDCOLOR}") 
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} introduces themselves and explains that {bcolors.RED}Mumbo{bcolors.ENDCOLOR} needs a specific block from him for some unknown reason...")
    spacer(1)
    print(f"{bcolors.GREEN}Grian{bcolors.ENDCOLOR} understands and heads over to his storage room and asks you to wait there. {bcolors.GREEN}Grian{bcolors.ENDCOLOR} heads off and after some time you hear a noise... you investigate and discover its a pesky skeleton! The skeleton readies its bow and aims at {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}... get ready!")
    spacer(1)
    sk_attack()
    spacer(1)
    print(f"{bcolors.GREEN}Grian{bcolors.ENDCOLOR} returns form the storage room and sees that {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} has taken down a skeleon! - {bcolors.GREEN}'Wow! You really can handle yourself... Here take this slime block and head back to {bcolors.RED}Mumbo{bcolors.ENDCOLOR}{bcolors.GREEN} as quick as you can.{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} thanks {bcolors.GREEN}Grian{bcolors.ENDCOLOR} and heads back to {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} place...")
    spacer(5)
    print(f"After some time and alot of walking, {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} returns to {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} place. {bcolors.RED}Mumbo{bcolors.ENDCOLOR} greets {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} and takes the item from them.")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} is curious as to why  {bcolors.RED}Mumbo{bcolors.ENDCOLOR} needs this specific item - {bcolors.RED}Mumbo {bcolors.ENDCOLOR} explains that it is for a flying mechanism to try and help get {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} home!")
    spacer(1)
    print(f"Some time passes as {bcolors.RED}Mumbo{bcolors.ENDCOLOR} crafts this machine to get {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} home. A concerned {bcolors.RED}Mumbo{bcolors.ENDCOLOR} speaks to {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} and informs them that the machine isnt working so they will have to find another way home...")
    spacer(1)
    print(f"{bcolors.RED}Mumbo{bcolors.ENDCOLOR} offers {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} a dispenser for their efforts and as a pittance gift for not getting the flying machine up and running...")
    spacer(1)
    mumbo_gift()
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} and {bcolors.RED}Mumbo{bcolors.ENDCOLOR} decide to rest for a while and pick up the situation later...")
    spacer(1)
    print(f"Later on the two brainstorm ideas and {bcolors.RED}Mumbo's{bcolors.ENDCOLOR} mind sparks! {bcolors.RED}'I FIGURED IT OUT... it may not work but we have to try...'{bcolors.ENDCOLOR} {bcolors.RED}Mumbo{bcolors.ENDCOLOR} scurries to the chest in view and pulls out 10 glowstone blocks and a bucket of water.")
    spacer(1)
    print(f"{bcolors.RED}'Now... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}{bcolors.RED}this is a theoretical portal, but we need to try it.'{bcolors.ENDCOLOR} {bcolors.RED}Mumbo{bcolors.ENDCOLOR} positions the blocks in a door like shape and pours the water bucket inside... {bcolors.RED}'Damn it, it hasnt wor-'{bcolors.ENDCOLOR} Just before {bcolors.RED}Mumbo{bcolors.ENDCOLOR} can finish his sentence, the portal begins to whir and glow!")
    spacer(1)
    print(f"{bcolors.RED}Mumbo{bcolors.ENDCOLOR} jumps with joy! {bcolors.RED}'ITS WORKED... ITS ACTUALLY WORKED'{bcolors.ENDCOLOR} {bcolors.RED}Mumbo{bcolors.ENDCOLOR} ushers {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} towards the portal and nods at {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} with a smile on his face... {bcolors.RED}'Thank you {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}{bcolors.RED} for your help! I hope this gets you home safe and I hope we cross paths again sometime...{bcolors.ENDCOLOR}")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} smiles back at {bcolors.RED}Mumbo{bcolors.ENDCOLOR} and heads through the portal!")
    spacer(5)

    if count == 15:
        final_level()

    elif count == 10:
        deathnote_level()
   
    else:
        count != 15
        print("You dont have enough xp, restarting level.")
        deathnote_level()


# deathnote level function start
def deathnote_level():
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} steps out of the portal they just entered... They look around to figure out just where exactly they have ended up")
    spacer(1)
    print (f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} decides to look at their remote, maybe it will tell them where they are this time... it reads...")
    spacer(5)
    print("""
    ·▄▄▄▄  ▄▄▄ . ▄▄▄· ▄▄▄▄▄ ▄ .▄   ▐ ▄       ▄▄▄▄▄▄▄▄ . ▄▄ 
    ██· ██ ▀▄.▀·▐█ ▀█ •██  ██▪▐█  •█▌▐█ ▄█▀▄ •██  ▀▄.▀· ██▌
    ▐█▪ ▐█▌▐▀▀▪▄▄█▀▀█  ▐█.▪██▀▀█  ▐█▐▐▌▐█▌.▐▌ ▐█.▪▐▀▀▪▄ ▐█·
    ██. ██ ▐█▄▄▌▐█▪ ▐▌ ▐█▌·██▌▐▀  ██▐█▌▐█▌.▐▌ ▐█▌·▐█▄▄▌ .▀ 
    ▀▀▀▀▀•  ▀▀▀  ▀  ▀  ▀▀▀ ▀▀▀ ·  ▀▀ █▪ ▀█▄▀▪ ▀▀▀  ▀▀▀   ▀ """)
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} doesn't remember watching this show recently... why are they here? {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Looks around for anything that could be useful in getting them home, they spot a black book in the distance. {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Approaches the book...")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Picks the book up and opens it up out of curiosity. The book is filled with random names, times of death and medical conditions like - heart attack... car crash... gunshot wound... Just what is this?")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} looks to the first page, it reads 'PROPERTY OF LIGHT YAGAMI'- {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} recognises the name but cant remember why... ")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} realises they picked it up upside down... They turn it over and read the title.... 'DEATH NOTE' - {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} Drops the book in fear and they feel a cold presence near by.")
    spacer(1)
    print(f"{bcolors.MAGENTA}'Hey... what do you think of the book...'{bcolors.ENDCOLOR} {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} turns around to see an upside down slender figure with a wide grin affixed to its face and piercing wide red eyes!")
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} is frozen with fear...")
    spacer(1)
    print(f"'{bcolors.MAGENTA}Whats the matter? Never seen a Shinigami before, names Ryuk - Nice to meet ya! I dropped that book just as you arrived, finders keepers. Its yours.... if you want it hahahaha - hmm why dont we play a game, if I win - you die. If you win - I'll give you a gift... what d'ya say kid, do we have a deal?{bcolors.ENDCOLOR}")
    spacer(1)
    ryuk_gift() 
    spacer(1)
    dice_roll()
    spacer(1)
    print(f"{bcolors.MAGENTA}'YOU'RE JUST LUCKY KID GAHHH... I guess I owe you this gift...' {bcolors.MAGENTA}Ryuk{bcolors.ENDCOLOR} goes to hand {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} the death note book. {bcolors.MAGENTA}Ryuk{bcolors.ENDCOLOR} pauses and throws the book over his shoulder and gives a very meniacal laugh.{bcolors.ENDCOLOR} ")
    spacer(1)
    print(f"{bcolors.MAGENTA}'Did you really think you'd best a shinigami? HAHAHAHA... Here take this apple, its my FAVOURITE food so you better like it'{bcolors.ENDCOLOR}")
    spacer(5)
    print("""
                                                                       .;:cl;                                                                        
                                                                       'kl,:od:.                                                                      
                                                                        :doo,.o:                                                                      
                                                                         ,xO; cl                                                                      
                                                                          cKx.,d'                                                                     
                                                                          ;xk;.ol..                                                                   
                                                   .';:clollllc:,.  .;ldxxxxOc cOdxxdoc'.          .........                                          
                                             .,lxxxdddxOkOXXXXNNXKkx0XNXX0d:dd'cc .:d0XX0xl;:llodkO0KKK0Okkkdc,.                                      
                                           'lOkc:,'.;okO0KKKKKKKKXXXXKKKKKKKX0;lo.:kKKKKKXNNNXKXXXXXKKK0Okd:;cddoo;.                                  
                                        ,lkKKOdoolokKKKKKKKKKKKKKKKKKKKKKKKKXK;:olOKKKKKKKKKKKKKKKKKKKKKKKKkooooookk:.                                
                                     .lOXNXKKKKKKKKKKKKKKKKXNNNNNNNNWNXKKKKKXK::dcOXKKKKXNNNNXKKKKKKKKKKKKKKKKKKKkodkko.                              
                                   .lKNXXKKKKKKKKKKKKKKKKKKXXXXXXXXXNNWNNXXNNNkxOkKNWNXNWNXXXKKKKKKKKKKKKKKKKKKKKKKOxdxOd.                            
                                  ,ONNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXNWWWNNOlcc:l0XNWMWXKKKKKKKKKK0kddk00OkkOKKKKKK0dlkO:                           
                                .dXNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXXKKKKK00OOKKKXXXKKKKKKKKK0o'.  ..'.. .,o0KKKKKOllOx.                         
                               ;ONXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl              :0KKKKK0o:k0;                        
                             .oNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKc               lKKKKKKKkd00;                       
                             cNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOc.             .xKKKKKKKK0KKc                      
                            ,0OkKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk;             ;0KKKKKKKKKXKc                     
                           'Ox'oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk'            .l0KKKKKKKK0KK:                    
                          .OO..xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl              ;OKKKKKKKK0XO.                   
                          lK:.dKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00KKKKKKKKKKKKKKKKKKKKKKO,              ;OKKKKKKK00Xd.                  
                         .Ox.lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOkKKKKKKKKKKKKKKKKKKKKKKKl              .oKKKKKKKKO0X:                  
                         ;XxcOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.              'OKKKKKKK0kKd.                 
                         oKldKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk'              .oKKKKKKKKxOK,                 
                        '0d,xXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO'               cKKKKKKKKdxX:                 
                        lX:'kXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO'              .xKKKKKKKKooXc                 
                       .kk.;0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.             .oKKKKKKKKO,lNc                 
                       :Xo cKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd.             'OKKKKKKK0c.oNc                 
                       lWo.lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd.             ;0KKKKKKK0;.xK,                 
                      .xX;.oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0o.           .xKKKKKKKKKl'kk.                 
                      .x0'.oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOdoc.      .dKKKKKKKKK0;;Ko                  
                       dK; lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkl,..,lkKKKKKKKKKXx.lX;                  
                       ;Xd.:0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00KKKKKKKKKKKKKl;Ox.                  
                       .dK:'kXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO:d0,                   
                        '0x.lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo'xO'                   
                         lKc:0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd'o0:                    
                         .OO:xXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk',0x.                    
                          lKdxKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,.oXc                     
                          .kX0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0c.:Kd.                     
                           :NNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.;Xk.                      
                           .xNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,.xK,                       
                            .OWXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0c.d0:                        
                             :XNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.cKc                         
                             .xWNKKKKKKKKKKXXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:;Od.                         
                              ,KWNKKKKKKXXNNNNNNNNNXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXxl0k.                          
                               cXMNKKKKXNNNNNNNNNNNNNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO:oXc                           
                               .oNWXKKXNNNNNNNNNNNNNNNNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl;Ox.                           
                                .oNWXKXNNNNNNNNNNNNNNNNNXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo:OO'                            
                                 .oNNXXNNNNNNNNNNNNNNNNNNNXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKdcOO'                             
                                  .oNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0ol0O'                              
                                    oWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOxKk.                               
                                    '0WNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXKKXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXKo.                                
                                     :KWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0OKK:                                  
                                      cXWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKKKKKKKKKKKKKKKKKKKKKKKKKKOd00:                                   
                                       'xNWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXKKKKKKKKKKKKKKKKK0xdOx'                                    
                                         :KWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXKKKKKKKKKKKKKKK00Ko.                                     
                                          ,kXWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKKKKKKKKKKKKXNKc                                       
                                            ,kNWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKXN0l.                                        
                                             .c0WWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKKKKKKKKXNKl.                                          
                                               .:okKNNWWWNNNNNNNNNNNNNWWWWWNNNNNNNNNNNNNWWWWNXKKKKKXNNN0o'                                            
                                                   .,d0KXNNXKKNNNNNNK0xldKNWWWWWWNNNWWNX0KNWWNXNNXKOdc,.                                              
                                                      .;::,'..',,,,'..   .:loxkkxxxdl:,...,;:,',,'.                                     """)
   
    spacer(1)
    print(f"{bcolors.YELLOW}{name}{bcolors.ENDCOLOR} takes the apple and {bcolors.MAGENTA}Ryuk{bcolors.ENDCOLOR} flys away into the distance, {bcolors.YELLOW}{name}{bcolors.ENDCOLOR}'s stomach rumbles, so they decide to take a bite of the apple. As soon as they bit the apple a portal appears in front of them... {bcolors.YELLOW}{name}{bcolors.ENDCOLOR} walks towards the portal and enters...")
    spacer(1)

    if count == 15:
        final_level()

    elif count == 10:
        youtube_level()

    else:
        count != 15
        print("You dont have enough xp, restarting level.")
        deathnote_level()

introduction()











  




