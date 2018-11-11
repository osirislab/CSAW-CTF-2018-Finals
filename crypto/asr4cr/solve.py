#stage 1 weiner's attack
#https://github.com/pablocelayes/rsa-wiener-attack

'''
Created on Dec 14, 2011
@author: pablocelayes
'''

import ContinuedFractions, Arithmetic 

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    return d


c = 45532901824779701378231663264317691918332830832727980686741777650350897654972731931906126487183695081149779754337211259576173166293099080026360210494238959275834930884772828914504790990220112618808803618718921284861471408452351387148489569208903847288964821402052254148148283550521299399412532966770835208456058835316550638049581681130969595007241458911654151363153992694300910445899304425484918330492562481928441188111780684754432851810943390386788371370446571697596730749234374112810876064553895009312729747803267970163376377525012371123934730259190839294187981333459364290514186662847699605450828212079377654174428

e = 56464345445116249098049045336807445234357883929066056160509800851174255932943697111857107660018784212036377880810894047380656549383278972198516300670834705016468999714250951486912600249341791051961539477938043350992976556533909606031953927579029664976360355357096884954199433767448339255264831657804069495212007831723081630922243488700092552780963937083647566868158843349870118898134140101603936510785879524001693384328179832659722334742169456879889671271238721506778301709871337885442564361586631293011137834137912109208181348656281720720627766394041913283080319450233438914935475856576320213363102937394294033243533

n = 144731657075172369458365253117444692939543043921858848859103787081029935571261433965575780267889126491908228025197396050544630151378291212236766311668806004054369644769305000545793583915353079764667366200180574291376348069728516020997330701012031222049248560650540529425983462590552767265793268609531384242005329075143421408062869554263876675060033088763864236117044254825364969220914682084657647653707895098928730418682497939953647008736234172764734833411879279956351555928480516439340800516536708422230087334841118192814828087714947355712947595518081579349585938062548316427420775872732829914145491413512568074735861

d = hack_RSA(e,n)

print "[*]Private Key: %s" % (str(d))

m = hex(pow(c,d,n)).strip("0x").strip("L")

flag1 = "".join([chr(int("0x"+m[i:i+2],16)) for i in range(0,len(m),2)])

print "[*]Flag1: %s" % (flag1)

#stage 2 RC4 vuln

msg = "FAKE{LC5_I3_FAK3_BUT_1T_1S_G00D_T0_KN0W}"

c1 = [ 206 , 220 , 76 , 109 , 97 , 54 , 177 , 150 , 19 , 0 , 232 , 112 , 128 , 175 , 140 , 36 , 85 , 217 , 49 , 9 , 159 , 14 , 119 , 24 , 148 , 96 , 179 , 21 , 204 , 5 , 189 , 251 ,77 , 26 , 75 , 210 , 198 , 157 , 131 , 86 ]

c2 = [ 206 , 209 , 70 , 111 , 97 , 40 , 177 , 151 , 19 , 0 , 232 , 112 , 130 , 221 , 134 , 83 , 85 , 217 , 49 , 9 , 159 , 14 , 119 , 24 , 148 , 96 , 179 , 21 , 204 , 5 , 189 , 251 ,77 , 26 , 75 , 210 , 198 , 157 , 131 , 86 ]

flag2 = "".join([chr(ord(msg[i]) ^ c1[i] ^ c2[i]) for i in range(len(msg))])

print "[*]Flag2: %s" % (flag2)
