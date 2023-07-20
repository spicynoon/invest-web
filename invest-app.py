import streamlit as st
from forex_python.converter import CurrencyRates

def invest(amount, rate, years, currency):
    c = CurrencyRates()
    converted_amount = c.convert('USD', currency, amount)
    total = converted_amount * (1 + rate/100)**years
    return total

def main():
    st.title('Platform Investasi')

    st.write('Masukkan detail investasi:')
    amount = st.number_input('Jumlah Investasi', min_value=0.0)
    rate = st.number_input('Tingkat Bunga Tahunan (%)', min_value=0.0)
    years = st.number_input('Jumlah Tahun', min_value=0.0, step=1.0)
    currency = st.selectbox('Pilih Mata Uang', ['USD', 'EUR', 'GBP', 'JPY', 'IDR'])

    if st.button('Hitung Hasil Investasi'):
        result = invest(amount, rate, years, currency)
        if currency == 'IDR':
            st.success(f'Nilai investasi Anda setelah {years} tahun: Rp {result:,.2f}')
        else:
            st.success(f'Nilai investasi Anda setelah {years} tahun: {result:.2f} {currency}')

    st.write('Fitur Tambahan:')
    show_chart = st.checkbox('Tampilkan Grafik Investasi')

    if show_chart:
        # Menampilkan grafik investasi
        values = [invest(amount, rate, i, currency) for i in range(int(years)+1)]
        st.line_chart(values)

    st.write('Catatan:')
    st.write('- Program ini menggunakan rumus bunga majemuk tahunan sederhana.')
    st.write('- Nilai investasi yang ditampilkan sudah disesuaikan dengan tingkat bunga dan mata uang yang dipilih.')

if __name__ == '__main__':
    main()