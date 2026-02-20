$fn = 50;

// outer box
// y parallel
color([0,0,0])
cube([5,255,5]);
translate([250,0,0])
color([0,0,0])
cube([5,255,5]);
translate([0,0,250])
color([0,0,0])
cube([5,255,5]);
translate([250,0,250])
color([0,0,0])
cube([5,255,5]);
// x parallel
color([0,0,0])
cube([255,5,5]);
translate([0,250,250])
color([0,0,0])
cube([255,5,5]);
translate([0,0,250])
color([0,0,0])
cube([255,5,5]);
translate([0,250,0])
color([0,0,0])
cube([255,5,5]);
// z parallel
color([0,0,0])
cube([5,5,255]);
translate([250,250,0])
color([0,0,0])
cube([5,5,255]);
translate([250,0,0])
color([0,0,0])
cube([5,5,255]);
translate([0,250,0])
color([0,0,0])
cube([5,5,255]);

// Yellow
intersection(){
    color([255/255,242/255,0])
    translate([255,242,0])
    sphere(15);
    cube(255);
}

// Orange
intersection(){
    color([255/255,127/255,39/255])
    translate([255,127,39])
    sphere(15);
    cube(255);
}

// Red
intersection(){
    color([237/255,28/255,36/255])
    translate([237,28,36])
    sphere(15);
    cube(255);
}

// Pink
intersection(){
    color([255/255,174/255,201/255])
    translate([255,174,201])
    sphere(15);
    cube(255);
}

// Violet
intersection(){
    color([163/255,73/255,164/255])
    translate([163,73,164])
    sphere(15);
    cube(255);
}

// Blue
intersection(){
    color([63/255,72/255,204/255])
    translate([63,72,204])
    sphere(15);
    cube(255);
}

// Light Blue
intersection(){
    color([0/255,162/255,232/255])
    translate([0,162,232])
    sphere(15);
    cube(255);
}

// Green
intersection(){
    color([34/255,177/255,76/255])
    translate([34,177,76])
    sphere(15);
    cube(255);
}

// Light Green
intersection(){
    color([181/255,230/255,29/255])
    translate([181,230,29])
    sphere(15);
    cube(255);
}

// Ochre
intersection(){
    color([255/255,201/255,14/255])
    translate([255,201,14])
    sphere(15);
    cube(255);
}

// Brown
intersection(){
    color([185/255,122/255,87/255])
    translate([185,122,87])
    sphere(15);
    cube(255);
}

// Black
intersection(){
    color([30/255,30/255,30/255])
    translate([30,30,30])
    sphere(15);
    cube(255);
}

// White
intersection(){
    color([225/255,225/255,225/255])
    translate([225,225,225])
    sphere(15);
    cube(255);
}

// Grey
intersection(){
    color([127/255,127/255,127/255])
    translate([127,127,127])
    sphere(15);
    cube(255);
}