// calcul de l'accumulateur sur l'image im de contours binaires
int [][] compute_hough(PImage im){
  rmax = ceil(sqrt(im.width*im.width + im.height*im.height));
  rmin = -rmax;
  nb_r = 2*rmax;
  float r = 0; int loc = 0;
  int indR;
  int [][] tab = new int[nb_Theta][nb_r];
  for(int y = 0; y < im.height; y++) {
    for(int x = 0; x < im.width; x++) {
      loc = y*im.width + x;
      if(im.pixels[loc] == blanc) { // Seuls les points de contours votent
        for(int indTheta = 0; indTheta < nb_Theta; indTheta++){
          float thetaD = map(indTheta, 0, nb_Theta, -90, 90);
          float thetaR = radians(thetaD);
          r = x*cos(thetaR) + y*sin(thetaR);
          indR = floor(map(r, rmin, rmax, 0, nb_r));
          tab[indTheta][indR] += 1; // Vote
        }
      }
    }
  }
  return tab;
}


// Calcul des lignes principales (accumulateur supérieur au seuil)
Vector<droite> compute_hough_lines(int [][] tab, int seuil_hough){
  Vector<droite> lines = new Vector<droite>();
  float theta, r;
  for(int indTheta = 0; indTheta < nb_Theta; indTheta++) {
    for(int indR = 0; indR < nb_r; indR++) {
      if(tab[indTheta][indR] > seuil_hough) {
        theta = map(indTheta, 0, nb_Theta, -90, 90);
        r = map(indR, 0, nb_r, rmin, rmax);
        droite d = new droite(r, theta, tab[indTheta][indR]);
        lines.add(d);
      }
    }
  }
  return lines;
}
