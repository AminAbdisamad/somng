import * as React from 'react';
// Loading
// Error
// Data

export type countryType = {
  name: string;
  capital: string;
  region: string;
  population: number;
  area: number;
  topLevelDomain: [string];
  alpha2Code: string;
  alpha3Code: string;
  callingCodes: [string];
  altSpellings: [string];
  subregion: string;
  latlng: [number];
  demonym: string;
  gini: null;
  timezones: [string];
  borders: [string];
  nativeName: string;
  numericCode: string;
  currencies: {};
  languages: Object;
  translations: {};
  flag: string;
  regionalBlocs: Object;
  cioc: string;
};
export interface ErrorType {
  error: string;
}
export default function useCountryInfo() {
  const [country, setCountry] = React.useState<countryType | null>(null);
  const [error, setError] = React.useState<ErrorType | null>(null);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch(`https://restcountries.eu/rest/v2/name/${input}`)
      .then((response) =>
        response.json().then((data) => {
          if (response.status === 200) {
            console.log(data.name);
            data.map((country: countryType) => setCountry(country));
          }

          setLoading(false);
        })
      )
      .catch((error) => setError(error));
  }, []);

  return { country, error, loading };
}
