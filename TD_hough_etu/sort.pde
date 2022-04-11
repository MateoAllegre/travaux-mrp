class SortDroites implements Comparator<droite> {
  public int compare(droite a, droite b) {
    return b.acc - a.acc;
  }
}
