def main():
    # ROOT histogramını oluştur ve doldur
    h = TH2F('h', 'py vs px;px;py', 40, -4, 4, 40, -4, 4)
    x, y = np.random.normal(0, 1, 50000), np.random.normal(0, 1, 50000)
    h[...] = np.histogram2d(x, y, bins=(40, 40), range=[[-4, 4], [-4, 4]])[0]

    # Çizim
    fig, ax = plt.subplots(figsize=(10, 8))
    hep.hist2dplot(h, ax=ax)
    
    # Projeksiyonları ekle
    hep.histplot(h.ProjectionX(), ax=ax, color='blue', alpha=0.5, label='px projection')
    hep.histplot(h.ProjectionY(), ax=ax, color='red', alpha=0.5, label='py projection')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()