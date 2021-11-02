import shapefile

w=shapefile.Writer('./soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("kaya","satu")
w.record("gitu","dua")
w.record("aja","tiga")
w.record("ngeluh","empat")



w.poly([[[3,1], [1,6], [5,6], [3,1]]])
w.poly([[[11,6], [9,1], [13,1], [11,6]]])
w.poly([[[8,11], [2,9], [2,13], [8,11]]])
w.poly([[[12,11], [17,13], [17,9], [12,11]]])