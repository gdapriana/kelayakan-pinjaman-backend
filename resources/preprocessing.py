def encode_pendapatan(pendapatan):
  return 0 if pendapatan == "rendah" else 1 if pendapatan == "sedang" else 2
def encode_usia(usia):
  return 0 if usia == "muda" else 1 if usia == "parobaya" else 2 if usia == "tua" else 3
def encode_tanggungan(tanggungan):
  return 0 if tanggungan == "sedikit" else 1 if tanggungan == "sedang" else 2
def encode_pengeluaran(pengeluaran):
  return 0 if pengeluaran == "rendah" else 1 if pengeluaran == "sedang" else 2
def encode_aset(aset):
  return 0 if aset == "sedikit" else 1 if aset == "sedang" else 2

def encode_durasi_peminjaman(durasi_peminjaman):
  return 0 if durasi_peminjaman == "pendek" else 1 if durasi_peminjaman == "sedang" else 2

def get_input(data):
  pendapatan  = float(data["pendapatan"])
  usia        = float(data["usia"])
  tanggungan  = float(data["tanggungan"])
  pengeluaran = float(data["pengeluaran"])
  aset        = float(data["aset"])
  durasi_peminjaman = float(data["durasi_peminjaman"])
  return pendapatan, usia, tanggungan, pengeluaran, aset, durasi_peminjaman

def preprocessing(dataset):
  df = dataset.rename(columns={"Pendapatan": "pendapatan",
                          "Usia": "usia",
                          "Tanggungan": "tanggungan",
                          "Pengeluaran": "pengeluaran",
                          "Aset": "aset",
                          "Durasi Peminjaman": "durasi_peminjaman",
                          "Kelayakan": "kelayakan"})

  df['pendapatan'] = df['pendapatan'].apply(encode_pendapatan)
  df['usia'] = df['usia'].apply(encode_usia)
  df['tanggungan'] = df['tanggungan'].apply(encode_tanggungan)
  df['pengeluaran'] = df['pengeluaran'].apply(encode_pengeluaran)
  df['aset'] = df['aset'].apply(encode_aset)
  df['durasi_peminjaman'] = df['durasi_peminjaman'].apply(encode_durasi_peminjaman)
  return df.to_numpy()