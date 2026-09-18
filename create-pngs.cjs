const fs = require('fs');
const zlib = require('zlib');

function crc32(buf) {
  let table = [];
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let k = 0; k < 8; k++) {
      c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    }
    table[i] = c >>> 0;
  }
  let crc = 0 ^ (-1);
  for (let i = 0; i < buf.length; i++) {
    crc = (crc >>> 8) ^ table[(crc ^ buf[i]) & 0xFF];
  }
  return (crc ^ (-1)) >>> 0;
}

function makeChunk(type, data) {
  const typeBuf = Buffer.from(type, 'ascii');
  const lenBuf = Buffer.alloc(4);
  lenBuf.writeUInt32BE(data.length, 0);
  const crcBuf = Buffer.alloc(4);
  const toCrc = Buffer.concat([typeBuf, data]);
  crcBuf.writeUInt32BE(crc32(toCrc), 0);
  return Buffer.concat([lenBuf, typeBuf, data, crcBuf]);
}

function createPng(width, height, getPixel) {
  const signature = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);

  // IHDR: width(4), height(4), bitDepth(1), colorType(1=6:RGBA), comp(1), filter(1), interlace(1)
  const ihdrData = Buffer.alloc(13);
  ihdrData.writeUInt32BE(width, 0);
  ihdrData.writeUInt32BE(height, 4);
  ihdrData[8] = 8;  // 8 bits per channel
  ihdrData[9] = 6;  // RGBA
  ihdrData[10] = 0;
  ihdrData[11] = 0;
  ihdrData[12] = 0;
  const ihdrChunk = makeChunk('IHDR', ihdrData);

  // Raw scanlines: width * 4 + 1 bytes per row
  const rowLen = width * 4 + 1;
  const rawData = Buffer.alloc(rowLen * height);

  for (let y = 0; y < height; y++) {
    const rowOffset = y * rowLen;
    rawData[rowOffset] = 0; // Filter: None
    for (let x = 0; x < width; x++) {
      const [r, g, b, a] = getPixel(x, y);
      const pxOffset = rowOffset + 1 + x * 4;
      rawData[pxOffset] = r;
      rawData[pxOffset + 1] = g;
      rawData[pxOffset + 2] = b;
      rawData[pxOffset + 3] = a;
    }
  }

  const idatData = zlib.deflateSync(rawData);
  const idatChunk = makeChunk('IDAT', idatData);
  const iendChunk = makeChunk('IEND', Buffer.alloc(0));

  return Buffer.concat([signature, ihdrChunk, idatChunk, iendChunk]);
}

// 1. Create logo.png (width: 460, height: 180)
const logoPng = createPng(460, 180, (x, y) => {
  // Let's create a clean white/transparent logo rendering
  // Background
  const bg = [255, 255, 255, 0];

  // Head & lightbulb icon area: x between 20 and 160, y between 20 and 160
  if (x >= 25 && x <= 165 && y >= 15 && y <= 165) {
    // Bulb glass circle center at (130, 85)
    const dBulb = Math.hypot(x - 130, y - 85);
    if (dBulb >= 36 && dBulb <= 44 && y <= 120) {
      return [27, 24, 33, 255]; // bulb outline
    }
    // Head profile left center at (70, 100)
    const dHead = Math.hypot(x - 70, y - 90);
    if (dHead >= 28 && dHead <= 36 && x <= 75) {
      return [27, 24, 33, 255]; // head outline
    }
    // Shoulder line
    if (y >= 140 && y <= 147 && x >= 30 && x <= 85) {
      return [27, 24, 33, 255];
    }
    // Bulb base
    if (y >= 122 && y <= 138 && x >= 115 && x <= 145 && (y % 6 < 3)) {
      return [27, 24, 33, 255];
    }
    // Bulb glow inside
    if (dBulb < 36 && y < 118) {
      return [255, 248, 220, 255];
    }
  }

  // INO Letters: green (#6bd34d = 107, 211, 77) with dark border (#278a1d = 39, 138, 29)
  // 'I': x: 195 - 225, y: 35 - 120
  if (x >= 195 && x <= 225 && y >= 35 && y <= 120) {
    const isBorder = (x <= 199 || x >= 221 || y <= 39 || y >= 116);
    return isBorder ? [39, 138, 29, 255] : [118, 220, 80, 255];
  }

  // 'N': x: 245 - 325, y: 35 - 120
  if (x >= 245 && x <= 325 && y >= 35 && y <= 120) {
    const isLeftBar = x >= 245 && x <= 268;
    const isRightBar = x >= 302 && x <= 325;
    // Diagonal
    const diagX = 250 + ((y - 35) / 85) * 60;
    const isDiag = Math.abs(x - diagX) <= 12;

    if (isLeftBar || isRightBar || isDiag) {
      const isBorder = (x <= 248 || x >= 322 || y <= 38 || y >= 117 || Math.abs(x - diagX) >= 9);
      return isBorder ? [39, 138, 29, 255] : [118, 220, 80, 255];
    }
  }

  // 'O': center at (375, 77), rx: 42, ry: 42
  const dO = Math.hypot((x - 375), (y - 77.5) * 1.0);
  if (dO <= 44 && dO >= 16) {
    const isBorder = (dO >= 40 || dO <= 20);
    return isBorder ? [39, 138, 29, 255] : [118, 220, 80, 255];
  }

  // Text subtitle 'TECHNIEK EN INSTALLATIE'
  // y between 142 and 158, x between 180 and 440
  if (y >= 142 && y <= 158 && x >= 185 && x <= 435) {
    // subtle pixel text bars
    if ((x + y) % 3 !== 0) {
      return [77, 82, 88, 240];
    }
  }

  return bg;
});

fs.writeFileSync('logo.png', logoPng);
fs.writeFileSync('public/logo.png', logoPng);

// 2. Create perilex-photo.png (400x400)
const perilexPng = createPng(400, 400, (x, y) => {
  // Soft rounded gradient background
  const rBg = Math.hypot(x - 200, y - 200);
  const gradVal = Math.min(255, Math.max(225, Math.floor(250 - rBg * 0.1)));
  let color = [gradVal, gradVal + 3, gradVal, 255];

  // Red cable curving from (40, 360) to (120, 220)
  const cableX = 40 + (360 - y) * 0.55;
  if (y >= 200 && y <= 370 && Math.abs(x - cableX) <= 14) {
    const rib = (y % 12 < 4);
    return rib ? [183, 28, 28, 255] : [229, 57, 53, 255];
  }

  // Plug Body (angled upper left)
  const dPlug = Math.hypot(x - 170, y - 130);
  if (dPlug <= 70) {
    // Plug face
    const dFace = Math.hypot(x - 190, y - 130);
    if (dFace <= 42) {
      // 4 pin positions
      const p1 = Math.hypot(x - 170, y - 110);
      const p2 = Math.hypot(x - 210, y - 110);
      const p3 = Math.hypot(x - 170, y - 150);
      const p4 = Math.hypot(x - 210, y - 150);
      const pCenter = Math.hypot(x - 190, y - 130);

      if (p1 <= 7 || p2 <= 7 || p3 <= 7 || p4 <= 7) {
        return [220, 225, 220, 255]; // metal pins
      }
      if (pCenter <= 5) {
        return [130, 138, 132, 255]; // center flat pin
      }
      return [240, 244, 240, 255]; // plug front
    }
    return [220, 226, 222, 255]; // plug housing
  }

  // Wall socket (bottom right: 200 to 360)
  if (x >= 210 && x <= 360 && y >= 200 && y <= 350) {
    const dSocketCenter = Math.hypot(x - 285, y - 275);
    if (dSocketCenter <= 50) {
      // 4 socket holes
      const h1 = Math.hypot(x - 265, y - 255);
      const h2 = Math.hypot(x - 305, y - 255);
      const h3 = Math.hypot(x - 265, y - 295);
      const h4 = Math.hypot(x - 305, y - 295);
      const hCenter = Math.abs(x - 285) <= 10 && Math.abs(y - 275) <= 4;

      if (h1 <= 6 || h2 <= 6 || h3 <= 6 || h4 <= 6 || hCenter) {
        return [40, 45, 42, 255]; // dark socket holes
      }
      return [235, 240, 236, 255];
    }
    // Socket frame
    const isFrameBorder = (x <= 214 || x >= 356 || y <= 204 || y >= 346);
    return isFrameBorder ? [200, 208, 202, 255] : [248, 250, 248, 255];
  }

  // Corner pill: 'PERILEX 16A'
  if (x >= 20 && x <= 150 && y >= 20 && y <= 52) {
    return [255, 255, 255, 240];
  }

  return color;
});

fs.writeFileSync('perilex-photo.png', perilexPng);
fs.writeFileSync('public/perilex-photo.png', perilexPng);

console.log('Generated logo.png and perilex-photo.png successfully!');
