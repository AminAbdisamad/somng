import * as React from 'react';
import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';

import useCountryInfo from '../component/CountryInfo';

export default function Home() {
  return (
    <div className={styles.container}>
      <main className={styles.main}></main>
    </div>
  );
}
