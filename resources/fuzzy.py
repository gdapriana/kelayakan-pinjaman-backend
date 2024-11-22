def fuzzification(pendapatan, usia, tanggungan, pengeluaran, aset):
  fuzz_pendapatan = [
    max(0, min(1, (3 - pendapatan) / 2 if 1 < pendapatan < 3 else 1 if pendapatan <= 1 else 0)),
    max(0, min(1, (pendapatan - 1) / 2 if 1 < pendapatan < 3 else 1 if 3 <= pendapatan <= 5 else (7 - pendapatan) / 2 if 5 < pendapatan < 7 else 0)),
    max(0, min(1, (pendapatan - 5) / 2 if 5 < pendapatan < 7 else 1 if pendapatan >= 7 else 0))
  ]
  fuzz_usia = [
    max(0, min(1, (30 - usia) / 10 if 20 < usia < 30 else 1 if usia <= 20 else 0)),
    max(0, min(1, (usia - 20) / 10 if 20 < usia < 30 else 1 if 30 <= usia <= 40 else (50 - usia) / 10 if 40 < usia < 50 else 0)),
    max(0, min(1, (usia - 40) / 10 if 40 < usia < 50 else 1 if 50 <= usia <= 60 else (70 - usia) / 10 if 60 < usia < 70 else 0)),
    max(0, min(1, (usia - 60) / 10 if 60 < usia < 70 else 1 if usia >= 70 else 0))
  ]
  fuzz_tanggungan = [
    max(0, min(1, (4 - tanggungan) / 2 if 2 < tanggungan < 4 else 1 if tanggungan <= 2 else 0)),
    max(0, min(1, (tanggungan - 2) / 2 if 2 < tanggungan < 4 else 1 if tanggungan == 4 else (6 - tanggungan) / 2 if 4 < tanggungan < 6 else 0)),
    max(0, min(1, (tanggungan - 4) / 2 if 4 < tanggungan < 6 else 1 if tanggungan >= 6 else 0))
  ]
  fuzz_pengeluaran = [
    max(0, min(1, (2 - pengeluaran) / 1 if 1 < pengeluaran < 2 else 1 if pengeluaran <= 1 else 0)),
    max( 0, min(1, (pengeluaran - 1) / 1 if 1 < pengeluaran < 2 else 1 if 2 <= pengeluaran <= 4 else ( 5 - pengeluaran ) / 1 if 4 < pengeluaran < 5 else 0)),
    max(0, min(1, ( pengeluaran - 4 ) / 1 if 4 < pengeluaran < 5 else 1 if pengeluaran >= 5 else 0))
  ]
  fuzz_aset = [
    max(0, min(1, ( 20 - aset ) / 10 if 10 < aset < 20 else 1 if aset <= 20 else 0)),
    max(0, min(1, (aset - 10) / 10 if 10 < aset < 20 else 1 if 20 <= aset <= 40 else ( 60 - aset ) / 20 if 40 < aset < 60 else 0)),
    max(0, min(1, (aset - 40) / 20 if 40 < aset < 60 else 1 if aset >= 60 else 0 ))
  ]
  return {
    "pendapatan": fuzz_pendapatan,
    "usia": fuzz_usia,
    "tanggungan": fuzz_tanggungan,
    "pengeluaran": fuzz_pengeluaran,
    "aset": fuzz_aset
  }


def inference(fuzzification_values, rules):
  z = []
  a = []
  pendapatan  = fuzzification_values["pendapatan"]
  usia        = fuzzification_values["usia"]
  tanggungan  = fuzzification_values["tanggungan"]
  pengeluaran = fuzzification_values["pengeluaran"]
  aset        = fuzzification_values["aset"]

  for rule in rules:
    alpha = min(
      pendapatan[rule[0]],
      usia[rule[1]],
      tanggungan[rule[2]],
      pengeluaran[rule[3]],
      aset[rule[4]])
    a.append(alpha)

    if rule[-1] == "Tidak Layak":
      z.append(90 if alpha == 0 else 10 if alpha == 1 else (90 - (alpha * (90 - 10))))
    if rule[-1] == "Layak"  :
      z.append(10 if alpha == 0 else 90 if alpha == 1 else ((alpha * (90 - 10)) + 10))

  return z, a

def defuzzification(z, a):
  upper = []
  for i in range(len(z)):
    upper.append(z[i] * a[i])
  return sum(upper) / sum(a)
