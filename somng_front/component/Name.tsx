interface NameType {
  name: string;
  age?: number;
}

export const NameTag = ({ name, age }: NameType) => {
  return (
    <div>
      {name} {age}
    </div>
  );
};

interface MetadataType {
  institutionName: string;
  date: string;
}

export const nowYouSeeMe = ({ a, b }: { a: number; b: number }) => {
  if (a === b) {
    return 'b';
  }
  return <h1>Have No idea what im doing here</h1>;
};

export default function greeting(message: string) {
  if (message === 'greeting') {
    return 'greeting';
  }
  if (message !== 'hi') {
    return 'hey there';
  }
  return 'Hello there';
}
