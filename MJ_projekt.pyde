def setup():
    size(400,400)
    textSize(120)
    textAlign (CENTER)
    background(255,0,255)
def draw():
    if keyPressed == True:
        fill(0)
        if keyCode==DOWN:
            pass
        if key == 'j':
          text("J", width/2 +100, height/2)
    else:
        fill(255)
    if mousePressed:
        text("M", width/2-100, height/2)
    #print(mouseX, mouseY)
    print(hex(get(height/2, width/2)))
    s = createShape()
    s.beginShape()
    s.fill(0, 255, 255)
    s.noStroke()
    s.vertex(100, height/3*2)
    s.vertex(width/2-50, height/3*2-50)
    s.vertex(width/2, height/3*2+50)
    s.endShape(CLOSE)
    shape(s, 25, 25)