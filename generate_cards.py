from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.utils import simpleSplit

W,H = A4
G=HexColor('#2E5D34'); CREAM=HexColor('#FFF8E7'); OR=HexColor('#E8590C'); SAND=HexColor('#C99A2E'); PU=HexColor('#7B4FB3'); GR=HexColor('#666666')
c = canvas.Canvas('Rock_Rangers_Clue_Cards.pdf', pagesize=A4)
c.setTitle('Rock Rangers - Printable Clue Cards'); c.setAuthor('Rock Rangers')

def para(x,y,text,font='Helvetica',size=10,width=200,lead=None,color=black):
    lead = lead or size+3
    c.setFont(font,size); c.setFillColor(color)
    for ln in simpleSplit(text,font,size,width):
        c.drawString(x,y,ln); y-=lead
    return y

def header(title,sub):
    c.setFillColor(G); c.rect(0,H-70,W,70,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',24); c.drawString(30,H-42,title)
    c.setFont('Helvetica',11); c.drawString(30,H-60,sub)

def face(cx,cy,r,col):
    c.setFillColor(col); c.circle(cx,cy,r,fill=1,stroke=0)
    c.setFillColor(white); c.circle(cx-r*.35,cy+r*.2,r*.22,fill=1,stroke=0); c.circle(cx+r*.35,cy+r*.2,r*.22,fill=1,stroke=0)
    c.setFillColor(black); c.circle(cx-r*.35,cy+r*.2,r*.1,fill=1,stroke=0); c.circle(cx+r*.35,cy+r*.2,r*.1,fill=1,stroke=0)
    c.setStrokeColor(black); c.setLineWidth(1.5); c.arc(cx-r*.4,cy-r*.5,cx+r*.4,cy,200,140)

# ---------- PAGE 1: Ranger Kit ----------
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
header('ROCK RANGERS: The Great Rock Crew Quest','Ranger Kit  |  Grade 8  |  Team: ______________________')
y=H-110
c.setFillColor(G); c.setFont('Helvetica-Bold',14); c.drawString(30,y,'Meet your guides'); y-=14
guides=[('IGNA the Lava Lizard',OR,'Igneous','"Born in fire, cooled by time!"','Clues: visible crystals, glassy, tiny holes'),
        ('SEDI the River Turtle',SAND,'Sedimentary','"Layer by layer, I deliver!"','Clues: layers, gritty grains, fossils, fizzes in acid'),
        ('META the Mole',PU,'Metamorphic','"Heat and pressure, change forever!"','Clues: bands, sparkly crystals, smooth sheets')]
bw=(W-60-20)/3
for i,(n,col,fam,cat,cl) in enumerate(guides):
    x=30+i*(bw+10)
    c.setFillColor(white); c.setStrokeColor(col); c.setLineWidth(2); c.roundRect(x,y-162,bw,162,8,fill=1,stroke=1)
    face(x+bw/2,y-40,28,col)
    c.setFillColor(col); c.setFont('Helvetica-Bold',10.5); c.drawCentredString(x+bw/2,y-86,n)
    c.setFillColor(black); c.setFont('Helvetica-Bold',10); c.drawCentredString(x+bw/2,y-100,fam+' rocks')
    para(x+8,y-114,cat,'Helvetica-Oblique',8.5,bw-16,10.5,GR)
    para(x+8,y-138,cl,'Helvetica',8.5,bw-16,10.5)
c.setFont('Helvetica-Oblique',7.5); c.setFillColor(GR); c.drawString(30,y-174,'(Teacher: paste your 3D cartoon character art over these placeholders.)')
y-=198
c.setFillColor(G); c.setFont('Helvetica-Bold',14); c.drawString(30,y,'Team roles'); y-=16
for r,d in [('Reader','reads each clue card aloud'),('Recorder','writes on the answer slip'),('Speaker','gives the Rock Pitch'),('Checker','finds evidence words, runs the app check (Round 3)'),('Scout (5th member)','helps any role and keeps time')]:
    c.setFillColor(black); c.setFont('Helvetica-Bold',10); c.drawString(40,y,r+':'); c.setFont('Helvetica',10); c.drawString(150,y,d); y-=14
y-=10
c.setFillColor(G); c.setFont('Helvetica-Bold',14); c.drawString(30,y,'How to play (20 minutes)'); y-=16
for t in ['ROUND 1 - Clue Hunt (6 min): read the 6 cards, pick a name and a family, circle one evidence word. No answers yet!',
          'ROUND 2 - Rock Pitch (4 min): your Speaker pitches ONE rock to a neighbor team for 45 seconds, then swap.',
          'ROUND 3 - Reveal and Echo (4 min): the answers are revealed. Say the name back, do the guide gesture, and check your score.',
          'FINISH (2 min): add up points and write one sentence on your exit ticket.']:
    y=para(40,y,t,'Helvetica',10,W-80,13); y-=3
y-=6
c.setFillColor(G); c.setFont('Helvetica-Bold',14); c.drawString(30,y,'Rock Pitch sentence frames'); y-=16
c.setFillColor(white); c.setStrokeColor(G); c.setLineWidth(1.5); c.roundRect(30,y-62,W-60,66,6,fill=1,stroke=1)
for i,t in enumerate(['"We believe Rock #__ is ________ because the clue says ________."','"It formed when ________________________________."','"It belongs to ________\'s family, the ________ rocks."']):
    c.setFillColor(black); c.setFont('Helvetica-Oblique',10.5); c.drawString(42,y-12-i*18,t)
c.showPage()

# ---------- PAGE 2: Clue Cards ----------
clues=[('The Crystal Mystery','Big, visible crystals in pink, gray and black. Very hard. Cooled slowly deep underground.'),
       ('The Floating Rock','Light and full of tiny holes. Cooled fast from lava. It can float on water!'),
       ('The Beach Rock','Feels gritty like a beach. Made of squeezed sand grains stacked in layers.'),
       ('The Shell Rock','Often has shell bits or fossils inside. Fizzes with weak acid.'),
       ('The Sparkle Rock','Shiny, sparkly crystals and no layers. It was once another rock, then baked and squeezed.'),
       ('The Page Rock','Flat, smooth sheets that split like pages. It was once mud, then squeezed.')]
mx=30; gap=14; cw=(W-2*mx-gap)/2; ch=(H-2*30-2*gap)/3
for i,(ttl,txt) in enumerate(clues):
    col,row=i%2,i//2
    x=mx+col*(cw+gap); yb=H-30-(row+1)*ch-row*gap
    c.setFillColor(white); c.setStrokeColor(G); c.setLineWidth(1.5); c.setDash(5,3); c.roundRect(x,yb,cw,ch,10,fill=1,stroke=1); c.setDash()
    c.setFillColor(G); c.roundRect(x+6,yb+ch-34,cw-12,28,6,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',13); c.drawString(x+14,yb+ch-25,f'ROCK CARD #{i+1}')
    c.setFont('Helvetica',9); c.drawRightString(x+cw-14,yb+ch-25,'Rock Rangers')
    c.setFillColor(HexColor('#F2F2F2')); c.setStrokeColor(GR); c.setDash(3,2); c.rect(x+12,yb+ch-132,cw-24,92,fill=1,stroke=1); c.setDash()
    c.setFillColor(GR); c.setFont('Helvetica-Oblique',9); c.drawCentredString(x+cw/2,yb+ch-88,'Paste rock photo here')
    c.setFillColor(G); c.setFont('Helvetica-Bold',11); c.drawString(x+14,yb+ch-148,ttl)
    para(x+14,yb+ch-162,txt,'Helvetica',10,cw-28,13)
    c.setFillColor(black); c.setFont('Helvetica',8.5); c.drawString(x+14,yb+14,'Ranger check:')
    for j,lab in enumerate(['Crystals','Layers','Bands']):
        bx=x+80+j*62; c.setStrokeColor(black); c.setLineWidth(1); c.rect(bx,yb+13,8,8,fill=0,stroke=1); c.drawString(bx+11,yb+14,lab)
c.showPage()

# ---------- PAGE 3: Team Answer Slip ----------
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
header('TEAM ANSWER SLIP','Lock in your answers BEFORE the reveal!   Team: ____________________')
y=H-95
c.setFillColor(white); c.setStrokeColor(G); c.setLineWidth(1.5); c.roundRect(30,y-34,W-60,38,6,fill=1,stroke=1)
c.setFillColor(G); c.setFont('Helvetica-Bold',10); c.drawString(40,y-10,'ROCK BANK:')
c.setFillColor(black); c.setFont('Helvetica',10.5); c.drawString(40,y-26,'Granite   Pumice   Basalt   Sandstone   Limestone   Shale   Marble   Slate')
y-=60
cols=[30,75,235,345,455,W-30]; heads=['Card','Rock name','Family','Evidence word','Pts (teacher)']
c.setFillColor(G); c.rect(30,y-20,W-60,22,fill=1,stroke=0); c.setFillColor(white); c.setFont('Helvetica-Bold',9.5)
for k,h in enumerate(heads): c.drawString(cols[k]+5,y-14,h)
y-=20; rh=36
for i in range(6):
    c.setFillColor(white if i%2==0 else HexColor('#F7F0DC')); c.setStrokeColor(GR); c.setLineWidth(.6); c.rect(30,y-rh,W-60,rh,fill=1,stroke=1)
    for k in range(1,5): c.line(cols[k],y,cols[k],y-rh)
    c.setFillColor(G); c.setFont('Helvetica-Bold',13); c.drawCentredString(52,y-22,f'#{i+1}')
    c.setFillColor(GR); c.setFont('Helvetica',8); c.drawString(cols[2]+5,y-12,'Igneous / Sedimentary /'); c.drawString(cols[2]+5,y-23,'Metamorphic (circle one)')
    c.drawRightString(W-38,y-22,'___ / 3')
    y-=rh
y-=24
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Round 2 - Rock Pitch notes (Speaker)'); y-=6
c.setFillColor(white); c.setStrokeColor(G); c.roundRect(30,y-62,W-60,64,6,fill=1,stroke=1); y-=84
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Round 3 - App check (Phone Ranger, optional)'); y-=16
for t in ['App guess: ______________________   Did it match our answer?   Yes   /   No','If not, who do we trust and why? ______________________________________________']:
    c.setFillColor(black); c.setFont('Helvetica',10); c.drawString(30,y,t); y-=18
y-=14
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Exit ticket (each student)'); y-=16
c.setFillColor(black); c.setFont('Helvetica',10); c.drawString(30,y,'Today I learned that ______________________ rocks form when ______________________________.')
y-=40
c.setFillColor(white); c.setStrokeColor(G); c.setLineWidth(1.5); c.roundRect(30,y-30,W-60,40,6,fill=1,stroke=1)
c.setFillColor(G); c.setFont('Helvetica-Bold',10.5); c.drawString(40,y-6,'SCORE:  Accuracy ___/18    Speaking ___/8    Teamwork ___/4    TOTAL ___/30')
c.setFont('Helvetica',9); c.drawString(40,y-22,'Badge: Gold 25-30  |  Silver 18-24  |  Bronze 10-17  |  Trainee <10')
c.showPage()

# ---------- PAGE 4: Teacher Key ----------
c.setFillColor(HexColor('#FFF1F0')); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(HexColor('#B3261E')); c.rect(0,H-70,W,70,fill=1,stroke=0)
c.setFillColor(white); c.setFont('Helvetica-Bold',22); c.drawString(30,H-40,'TEACHER ONLY - Answer Key and Scoring')
c.setFont('Helvetica',11); c.drawString(30,H-58,'Do not print this page for students. Reveal AFTER Round 2.')
y=H-100
key=[('1','Granite','Igneous (intrusive)','Igna','Slow cooling = big crystals'),('2','Pumice','Igneous (extrusive)','Igna','Fast cooling + gas bubbles = light, can float'),
     ('3','Sandstone','Sedimentary (clastic)','Sedi','Cemented sand grains in layers'),('4','Limestone','Sedimentary (chemical/organic)','Sedi','Shell/fossil material; fizzes in acid'),
     ('5','Marble','Metamorphic (non-foliated)','Meta','Limestone + heat and pressure = interlocking crystals'),('6','Slate','Metamorphic (foliated)','Meta','Shale/mud + pressure = splits into sheets')]
cx=[30,60,150,310,365]; 
c.setFillColor(G); c.rect(30,y-18,W-60,20,fill=1,stroke=0); c.setFillColor(white); c.setFont('Helvetica-Bold',9.5)
for k,h in enumerate(['#','Rock','Family','Guide','Reveal line']): c.drawString(cx[k]+4,y-12,h)
y-=18
for r in key:
    c.setFillColor(white); c.setStrokeColor(GR); c.setLineWidth(.6); c.rect(30,y-26,W-60,26,fill=1,stroke=1)
    c.setFillColor(black); c.setFont('Helvetica-Bold',10); c.drawString(cx[0]+4,y-17,r[0]); c.drawString(cx[1]+4,y-17,r[1])
    c.setFont('Helvetica',8.5); c.drawString(cx[2]+4,y-17,r[2]); c.drawString(cx[3]+4,y-17,r[3])
    c.setFont('Helvetica',8); c.drawString(cx[4]+4,y-12,r[4][:48]); 
    if len(r[4])>48: c.drawString(cx[4]+4,y-22,r[4][48:])
    y-=26
y-=12
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Scoring (30 points)'); y-=15
for t in ['Accuracy (18): per card, 1 pt rock name + 1 pt family + 1 pt valid evidence word (6 cards).',
          'Speaking (8): 0-2 each for clear claim, uses evidence, scientific vocabulary, clear voice/eye contact.',
          'Teamwork (4): 2 pts if every role used; 2 pts if every member spoke at least one sentence.',
          'Bonus (+1): a team that spots an app mistake in Round 3 and explains why.']:
    y=para(36,y,t,'Helvetica',9.5,W-72,12.5); y-=2
y-=8
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Echo gestures (Round 3)'); y-=15
for t in ['Igna: wiggle fingers upward like flames.   Sedi: stack your hands layer by layer.   Meta: squeeze your fists together.']:
    y=para(36,y,t,'Helvetica',9.5,W-72,12.5)
y-=10
c.setFillColor(G); c.setFont('Helvetica-Bold',12); c.drawString(30,y,'Printing notes'); y-=15
for t in ['Print pages 1-3 in color; make 9 sets (8 teams of 4 + 1 team of 5 = 37 students). Cut page 2 along the dashed lines.',
          'Paste real photos from your own samples or Wikimedia Commons into the gray boxes before copying.',
          'Pages are A4. Paper-only teams are never at a disadvantage: the app check in Round 3 is optional.']:
    y=para(36,y,t,'Helvetica',9.5,W-72,12.5); y-=2
c.showPage(); c.save()
